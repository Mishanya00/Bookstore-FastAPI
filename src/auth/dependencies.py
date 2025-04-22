import re

from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer


EMAIL_PATTERN = r"\b[\w\-\.]+@(?:[\w-]+\.)+[\w\-]{2,4}\b"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


def validate_email(email: str) -> str:
    if not re.fullmatch(EMAIL_PATTERN, email):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Invalid email format")
    return email


async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        pass
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
