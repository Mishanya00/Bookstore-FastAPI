from typing import Annotated

from fastapi import APIRouter, Body

from src.auth.schemas import UserRegisterSchema


auth_router = APIRouter()


@auth_router.post("/register")
async def register_user(user: Annotated[UserRegisterSchema, Body()]):
    return user