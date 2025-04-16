from src.exceptions import BaseAppException


class UserExistError(BaseAppException):
    def __init__(self, message: str):
        super().__init__(message, status_code=409)