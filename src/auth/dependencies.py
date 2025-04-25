from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer

from jwt.exceptions import InvalidTokenError

from src.auth.service import decode_access_token
from src.auth.schemas import UserSchema
from src.db.queries import get_user_by_email
from src.auth.exceptions import UserCredentialsException


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = decode_access_token(token)
        email = payload.get("sub")
        if email is None:
            raise UserCredentialsException
        user = await get_user_by_email(email)
        if user is None:
            raise UserCredentialsException
        return UserSchema(**user)
    except InvalidTokenError:
        raise UserCredentialsException
