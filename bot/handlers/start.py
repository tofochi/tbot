from aiogram import F, Router, types
from aiogram.filters import CommandStart

from handlers import main_menu

router = Router()

@router.message(CommandStart())
async def start(message: types.Message) -> None:
    await message.answer(f"Hello, {message.from_user.first_name}!",
                         reply_markup=main_menu())