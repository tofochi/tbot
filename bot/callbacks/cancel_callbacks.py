from aiogram import types, Router, F


from callbacks import (text_find_menu)
from callbacks import (text_main_menu_start)

from callbacks import first_name_is_none, last_name_is_none
from callbacks import main_menu, find_menu, admin_menu, text_admin_menu


router = Router()

@router.callback_query(F.data == "find_menu:cancel_to_main_menu")
async def callback_data_find_menu_cancel(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text(text=f"{text_main_menu_start(
        name=callback.from_user.first_name, 
        lastname=callback.from_user.last_name)}", reply_markup=main_menu())


@router.callback_query(F.data == "find_menu:cancel_to_find_menu")
async def callback_data_find_menu_cancel(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text(text=text_find_menu(), reply_markup=find_menu())


@router.callback_query(F.data == "main_menu:cancel")
async def callback_data_main_menu_cancel(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text(text=f"{text_main_menu_start(
        name=first_name_is_none(callback.from_user.first_name), 
        lastname=last_name_is_none(callback.from_user.last_name))}", reply_markup=main_menu())


@router.callback_query(F.data == "admin_menu:cancel")
async def callback_data_admin_menu_cancel(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text(text=text_admin_menu(
        name=first_name_is_none(callback.from_user.first_name),
        lastname=last_name_is_none(callback.from_user.last_name)),
        reply_markup=admin_menu()
    )