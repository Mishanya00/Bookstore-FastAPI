from typing import Annotated

from fastapi import APIRouter, Body, Depends, HTTPException, status

from src.auth.schemas import UserFormSchema
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

from src.auth.exceptions import UserExistError
from src.auth import service
from src.auth.dependencies import validate_email


auth_router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


@auth_router.post("/register")
async def register_user(user: Annotated[UserFormSchema, Body()]):
    if await service.register_user(user):
        return {'message': 'user is registered!'}


@auth_router.post("/login")
async def login_user(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = await service.authenticate_user(form_data.username, form_data.password)
    if user:
        return user
    return {'error': 'invalid username or password'}


@auth_router.get("/get_user/{email}")
async def get_user(email: Annotated[str, Depends(validate_email)]):
    user = await service.get_user(email)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="user does not exist"
        )
    return user
