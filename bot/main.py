# other imports
import asyncio
import logging

# aiogram imports
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

# aiogram routers imports
from handlers import start, admin

from callbacks import main_menu_callback, find_menu_callback, cancel_callbacks, admin_menu_callbacks

from database.database import Database

# config imports
from config import load_settings, check_settings


logging.basicConfig(level=logging.INFO)

settings = load_settings()

check_settings()

bot = Bot(token=settings.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp = Dispatcher()
db = Database() # initialize Class Database


# include routers
# ПРИМЕЧАНИЕ!!! Если создал новый файл, то добавь его роутер, иначе весь код в этом файле не будет работать
dp.include_router(start.router) # к примеру вот так
dp.include_router(admin.router)

dp.include_router(main_menu_callback.router)
dp.include_router(find_menu_callback.router)
dp.include_router(cancel_callbacks.router)
dp.include_router(admin_menu_callbacks.router)


async def main() -> None:
    await db.create_db() # create database
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(" ")


# 1) TODO: Доделать админ панель (хотя бы половину)