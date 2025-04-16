from typing import Annotated

from fastapi import APIRouter, Body, Depends, HTTPException, status

from src.auth.schemas import UserFormSchema

from src.auth.exceptions import UserExistError
from src.auth import service
from src.auth.dependencies import validate_email


auth_router = APIRouter()


@auth_router.post("/register")
async def register_user(user: Annotated[UserFormSchema, Body()]):
    await service.register_user(user)


@auth_router.get("/get_user/{email}")
async def get_user(email: Annotated[str, Depends(validate_email)]):
    user = await service.get_user(email)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="user does not exist"
        )
    return user
