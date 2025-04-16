from psycopg import rows

from src.config import DB_CONFIG
from src.db.core import get_db_connection


async def get_user_by_email(email: str):
    async with get_db_connection(DB_CONFIG) as aconn:
        # rows.dict_row to generate dictionary as a result of query
        async with aconn.cursor(row_factory=rows.dict_row) as acur:
            sql = """
                    SELECT email, hashed_password, money FROM users
                    WHERE email = %s
                """
            await acur.execute(sql, [email])
            record = await acur.fetchone()
            return record


async def create_user(email: str, password_hash: str):
    async with get_db_connection(DB_CONFIG) as aconn:
        async with aconn.cursor() as acur:
            sql = f"""
                    INSERT INTO users(email, hashed_password)
                    VALUES ('{email}', '{password_hash}')
                """
            await acur.execute(sql)
        await aconn.commit()
