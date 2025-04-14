from fastapi import HTTPException
import re


EMAIL_PATTERN = r"\b[\w\-\.]+@(?:[\w-]+\.)+[\w\-]{2,4}\b"


def validate_email(email: str) -> str:
    if not re.fullmatch(EMAIL_PATTERN, email):
        raise HTTPException(status_code=422, detail="Invalid email format")
    return email
