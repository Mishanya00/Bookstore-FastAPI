from typing import Annotated

from fastapi import APIRouter, Body, Depends, HTTPException, status

from src.auth.schemas import UserRegisterSchema

from src.auth import service
from src.auth.dependencies import validate_email


auth_router = APIRouter()


@auth_router.post("/register")
async def register_user(user: Annotated[UserRegisterSchema, Body()]):
    try:
        await service.register_user(user)
    except HTTPException:
        raise
    except Exception as e:
        print(f"Server error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from e


@auth_router.get("/get_user/{email}")
async def get_user(email: Annotated[str, Depends(validate_email)]):
    user = await service.get_user(email)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="user does not exist"
        )
    return user
