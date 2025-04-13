from typing import Annotated

from fastapi import APIRouter, Body, Depends

from src.auth.schemas import UserRegisterSchema

from src.auth import service
from src.auth.dependencies import validate_email


auth_router = APIRouter()


@auth_router.post("/register")
async def register_user(user: Annotated[UserRegisterSchema, Body()]):
    await service.register_user(user)


@auth_router.get("/get_user/{email}")
async def get_user(email: Annotated[str, Depends(validate_email)]):
    return email