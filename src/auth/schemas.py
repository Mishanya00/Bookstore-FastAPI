from typing import Annotated

from pydantic import BaseModel, Field


EMAIL_PATTERN = r"\b[\w\-\.]+@(?:[\w-]+\.)+[\w\-]{2,4}\b"


class UserRegisterSchema(BaseModel):
    email: Annotated[str, Field(max_length = 64, pattern=EMAIL_PATTERN)]
    password: Annotated[str, Field(min_length=8)]


class UserSchema(BaseModel):
    email: str
    password_hash: Annotated[str, Field(exclude=True)]
    money: float