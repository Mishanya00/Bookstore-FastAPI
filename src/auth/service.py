import hashlib
from datetime import datetime, timedelta, timezone

from psycopg.errors import UniqueViolation  
from fastapi import HTTPException, status
import jwt

from src.auth.exceptions import UserExistException, UserNotExistException, IncorrectCredentialsException
from src.auth.schemas import UserFormSchema, UserSchema
from src.db import queries
from src.config import JWT_SECRET, JWT_REFRESH_SECRET, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, REFRESH_TOKEN_EXPIRE_MINUTES


def verify_password(plain_password: str, hashed_password: str) -> bool:
    if hashlib.sha256(plain_password.encode()).hexdigest() == hashed_password:
        return True
    return False


def create_jwt(data: dict, expires_delta: timedelta, secret: str) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, secret, algorithm=ALGORITHM)


def create_access_token(data: dict) -> str:
    return create_jwt(data, timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES), JWT_SECRET)


def create_refresh_token(data: dict) -> str:
    return create_jwt(data, timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES), JWT_REFRESH_SECRET)


async def register_user(user: UserFormSchema):
    hashed_password = hashlib.sha256(user.password.encode()).hexdigest()
    try:
        await queries.create_user(user.email, hashed_password)
        return True
    except UniqueViolation as e:
        raise UserExistException('User already exists') from e


async def is_user_exist(email: str) -> bool:
    user_data = await queries.get_user_by_email(email)
    if user_data:
        return True
    return False


async def get_user(email: str) -> UserSchema | None:
    user_data = await queries.get_user_by_email(email)
    if user_data is None:
        raise UserNotExistException('User does not exist')
    return UserSchema(**user_data)


async def authenticate_user(email: str, password: str) -> UserSchema | None:
    # user_data = await queries.get_user_by_email(email)
    user = await get_user(email)
    if not user:
        raise UserNotExistException('User does not exist')
    if not verify_password(password, user.hashed_password):
        raise IncorrectCredentialsException('Incorrect password')
    return user