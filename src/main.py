import asyncio
import sys

from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.db.init_db import create_tables
from src.books.routes import book_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()

    yield
    
    print('Application is shut down')


app = FastAPI(lifespan=lifespan)

app.include_router(book_router, prefix='/books', tags=["books"])

