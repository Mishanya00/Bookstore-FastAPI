from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.exceptions import BaseAppException
from src.db.init_db import create_tables

from src.books.routes import book_router
from src.auth.routes import auth_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()

    yield
    
    print('Application is shut down')


app = FastAPI(lifespan=lifespan)

app.include_router(book_router, prefix='/books', tags=["books"])
app.include_router(auth_router, prefix='/auth', tags=['auth'])


@app.exception_handler(BaseAppException)
async def app_exception_handler(request: Request, err: BaseAppException):
    return JSONResponse(
        status_code=err.status_code,
        content={"error": err.message}
    ) 

