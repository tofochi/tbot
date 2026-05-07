from aiogram import F, Router, types
from aiogram.filters import CommandStart

from handlers import main_menu
from handlers import text_start

router = Router()

@router.message(CommandStart())
async def start(message: types.Message) -> None:
    await message.answer(
        text_start(
            name=message.from_user.first_name,
            lastname=message.from_user.last_name,
        ),
        reply_markup=main_menu(),
    )