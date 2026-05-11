from aiogram import types, Router
from aiogram.filters import Command

from handlers import admin_menu


router = Router()


@router.message(Command("admin"))
async def admin(message: types.Message) -> None:
    await message.answer(text="Админ панель. Выбери действие ниже",
                         reply_markup=admin_menu())
