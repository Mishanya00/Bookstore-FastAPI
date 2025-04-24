from src.exceptions import BaseAppException


class UserExistException(BaseAppException):
    def __init__(self, message: str):
        super().__init__(message, status_code=409)


class UserNotExistException(BaseAppException):
    def __init__(self, message: str):
        super().__init__(message, status_code=401)


class IncorrectCredentialsException(BaseAppException):
    def __init__(self, message: str):
        super().__init__(message, status_code=401)