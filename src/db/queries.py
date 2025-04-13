from psycopg import AsyncConnection

from src.config import DB_CONFIG
from src.db.core import get_db_connection


async def get_user_by_email(email: str):
    async with get_db_connection(DB_CONFIG) as aconn:
        async with aconn.cursor() as acur:
            sql = f"""
                    SELECT email, hashed_password, money FROM users
                    WHERE email = '{email}'
                """
            await acur.execute(sql)
            return await acur.fetchone()


async def create_user(email: str, password_hash: str):
    async with get_db_connection(DB_CONFIG) as aconn:
        async with aconn.cursor() as acur:
            sql = f"""
                    INSERT INTO users(email, hashed_password)
                    VALUES ('{email}', '{password_hash}')
                """
            await acur.execute(sql)
        await aconn.commit()