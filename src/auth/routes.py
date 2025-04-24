from typing import Annotated

from fastapi import APIRouter, Body, Depends, HTTPException, status

from src.auth.schemas import UserFormSchema, UserSchema, TokenSchema
from fastapi.security import OAuth2PasswordRequestForm

from src.auth import service
from src.auth.dependencies import validate_email, get_current_user
from src.exceptions import BaseAppException

auth_router = APIRouter()


@auth_router.post("/register")
async def register_user(user: Annotated[UserFormSchema, Body()]):
    try:
        await service.register_user(user)
        return {'message': 'user is registered!'}
    except BaseAppException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))


@auth_router.post("/login")
async def login_user(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> TokenSchema:
    try:
        user = await service.authenticate_user(form_data.username, form_data.password)
        access_token = service.create_access_token({
                "sub": user.email,
                "type": "access",
            })
        refresh_token = service.create_refresh_token({
            "sub": user.email,
            "type": "refresh",
        })
        return TokenSchema(access_token=access_token, refresh_token=refresh_token, token_type="bearer")
    except BaseAppException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))


@auth_router.get("/me")
async def get_user(curr_user: Annotated[UserSchema, Depends(get_current_user)]):
    pass