import psycopg
from src.db.core import get_db_connection
from src.config import DB_CONFIG


async def create_tables():
    async with get_db_connection(DB_CONFIG) as aconn:
        try:
            async with aconn.cursor() as acur:
                await acur.execute('''
                    CREATE TABLE authors (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(255) NOT NULL               
                    )
                    ''')
            await aconn.commit()
        except psycopg.errors.DuplicateTable:
            print('table authors has already been created')