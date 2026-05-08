import aiosqlite

async def create_db() -> None:
    async with aiosqlite.connect("database/dbs/users.db") as db:
        await db.execute(
            """CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            balance INTEGER NOT NULL,
            requests INTEGER NOT NULL,
            subscription_status INTEGER NOT NULL,
            subscription_until DATE,
            """

        )

# id - 0, 1, 2, 3...
# user_id - 123001528, 2183488224, 21398921492
# balance - 100, 1000, 10000...
# requests - 1, 50, 1000...