from aiogram import Router, types
from aiogram.filters import CommandStart

from handlers import (main_menu,
                      first_name_is_none,
                      last_name_is_none,
                      text_main_menu_start,
                      db)



router = Router()

@router.message(CommandStart())
async def start(message: types.Message) -> None:
    await db.add_user(message.from_user.id)
    await message.answer(
        text_main_menu_start(
            name=first_name_is_none(message.from_user.first_name),
            lastname=last_name_is_none(message.from_user.last_name),
        ),
        reply_markup=main_menu(),
    )
