from fastapi import APIRouter


book_router = APIRouter()


@book_router.get("/show")
async def show_books():
    return {
        'book1': 'author1',
        'book2': 'author2',
        'book3': 'author3',
    }
