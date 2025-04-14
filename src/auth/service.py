import hashlib

from fastapi import HTTPException, status

from src.auth.schemas import UserRegisterSchema, UserSchema

from src.db import queries


async def register_user(user: UserRegisterSchema):
    hashed_password = hashlib.sha256(user.password.encode()).hexdigest()
    await queries.create_user(user.email, hashed_password)


async def get_user(email: str) -> UserSchema | None:
    user_data = await queries.get_user_by_email(email)
    return UserSchema(**user_data) if user_data else None
