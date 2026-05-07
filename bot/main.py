# other imports
import asyncio
import logging

# aiogram imports
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher, F, types
from aiogram.client.default import DefaultBotProperties

# aiogram routers imports
from handlers import start
from callbacks import callback

# config imports
from config import load_settings, check_settings


logging.basicConfig(level=logging.INFO)

settings = load_settings()

check_settings()

bot = Bot(token=settings.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

# include routers
# ПРИМЕЧАНИЕ!!! Если создал новый файл, то добавь его роутер, иначе весь код в этом файле не будет работать
dp.include_router(start.router) # к примеру вот так
dp.include_router(callback.router)


async def main() -> None:

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(" ")