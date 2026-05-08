from datetime import datetime
from typing import Optional

from database import db_date_to_iso_format, db_iso_format_to_date

import aiosqlite


class Database:
    def __init__(self):
        self.path = "database/dbs/users.db"

    async def create_db(self) -> None:
        async with aiosqlite.connect(self.path) as db:
            await db.execute(
                """CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                balance INTEGER NOT NULL,
                requests INTEGER NOT NULL,
                subscription_status BOOLEAN NOT NULL,
                subscription_until DATE
                )"""
            )
            await db.commit()

    async def get_user(self, user_id: int) -> aiosqlite.Row | None:
        async with aiosqlite.connect(self.path) as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute("SELECT user_id FROM users WHERE user_id = ?", (user_id,))
            return await cursor.fetchone()


    async def add_user(self, user_id: int,
                       balance: int = 0,
                       requests: int = 0,
                       subscription_status: bool = False,
                       subscription_until: Optional[datetime] = None) -> bool:
        async with aiosqlite.connect(self.path) as db:
            if not await self.get_user(user_id):
                sub_until_str = db_date_to_iso_format(subscription_until)
                # date -> iso    datetime(2001, 1, 1, 11, 11, 11) -> 2001-01-01T11:11:11
                # iso -> date    2001-01-01T11:11:11 -> datetime(2001, 1, 1, 11, 11, 11)
                await db.execute("INSERT INTO users(user_id, balance, requests, subscription_status, subscription_until) VALUES (?, ?, ?, ?, ?)",
                                 (user_id, balance, requests, subscription_status, sub_until_str))
                await db.commit()
            return True


    async def update_data(self, user_id: int,
                          balance: int,
                          requests: int,
                          subscription_status: bool,
                          subscription_until: Optional[datetime]
                          ):

        async with aiosqlite.connect(self.path) as db:
            sub_until_str = db_date_to_iso_format(subscription_until)
            await db.execute("UPDATE users SET balance = ?, requests = ?, subscription_status = ?, subscription_until = ? WHERE user_id = ?",
                             (balance, requests, subscription_status, sub_until_str, user_id))
            await db.commit()


db = Database()

# id - 0, 1, 2, 3...
# user_id - 123001528, 2183488224, 21398921492
# balance - 100, 1000, 10000...
# requests - 1, 50, 1000...