import asyncio
import logging

from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher, F, types
from aiogram.client.default import DefaultBotProperties

from config import load_settings, check_settings


logging.basicConfig(level=logging.INFO)

settings = load_settings()

bot = Bot(token=settings.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


async def main() -> None:
    check_settings()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(" ")