import hashlib

from src.auth.schemas import UserRegisterSchema, UserSchema

from src.db import queries


async def register_user(user: UserRegisterSchema):
    hashed_password = hashlib.sha256(user.password.encode()).hexdigest()
    await queries.create_user(user.email, hashed_password)


async def get_user(email: str) -> UserSchema | None:
    user_data = await queries.get_user_by_email(email)
    print(user_data)
    # user = UserSchema(user_data)
    return user_data