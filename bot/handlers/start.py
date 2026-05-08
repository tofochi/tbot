from aiogram import F, Router, types
from aiogram.filters import CommandStart

from handlers import main_menu
from handlers import text_main_menu_start

from other.check import first_name_is_none, last_name_is_none

router = Router()

@router.message(CommandStart())
async def start(message: types.Message) -> None:
    await message.answer(
        text_main_menu_start(
            name=first_name_is_none(message.from_user.first_name),
            lastname=last_name_is_none(message.from_user.last_name),
        ),
        reply_markup=main_menu(),
    )