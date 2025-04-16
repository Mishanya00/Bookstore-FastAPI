import hashlib

from psycopg.errors import UniqueViolation  
from fastapi import HTTPException, status

from src.auth.exceptions import UserExistError
from src.auth.schemas import UserFormSchema, UserSchema
from src.db import queries


async def register_user(user: UserFormSchema):
    hashed_password = hashlib.sha256(user.password.encode()).hexdigest()
    try:
        await queries.create_user(user.email, hashed_password)
    except UniqueViolation as e:
        raise UserExistError('User already exists') from e


async def is_user_exist(email: str) -> bool:
    user_data = await queries.get_user_by_email(email)
    if user_data:
        return True
    return False


async def get_user(email: str) -> UserSchema | None:
    user_data = await queries.get_user_by_email(email)
    return UserSchema(**user_data) if user_data else None
