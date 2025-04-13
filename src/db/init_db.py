import psycopg
from src.db.core import get_db_connection
from src.config import DB_CONFIG


async def create_tables():

    commands = (
        """CREATE TABLE authors (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        )""",
        
        """CREATE TABLE books (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            author_id INTEGER REFERENCES authors(id) ON DELETE CASCADE,
            price DECIMAL(10, 2) NOT NULL,
            amount INTEGER NOT NULL
        )""",

        """CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            email VARCHAR(255) UNIQUE NOT NULL,
            hashed_password VARCHAR(255) NOT NULL,
            money DECIMAL(10, 2) DEFAULT 0.00
        )""",

        """CREATE TABLE user_books (
            user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
            book_id INTEGER REFERENCES books(id) ON DELETE CASCADE,
            purchase_date TIMESTAMP DEFAULT NOW(),
            PRIMARY KEY (user_id, book_id)
        )"""
    )

    async with get_db_connection(DB_CONFIG) as aconn:
        for command in commands:
            try:
                async with aconn.cursor() as acur:
                    await acur.execute(command)
                    await aconn.commit()
            except psycopg.errors.DuplicateTable:
                print(f"table {command.split()[2]} already exists")
                await aconn.rollback()
            except Exception as e:
                print(f"Error executing command: {e}")
                await aconn.rollback()
                raise
