from aiogram import types, Router, F

from callbacks import text_info, text_sub, text_start
from callbacks import main_menu_cancel, main_menu

router = Router()

@router.callback_query(F.data == "main_menu:profile")
async def callback_data_profile(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text("soon...", reply_markup=main_menu_cancel()) # return profile


@router.callback_query(F.data == "main_menu:buy_sub")
async def callback_data_buy_sub(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text(f"{text_sub()}", reply_markup=main_menu_cancel()) # return subscription menu


@router.callback_query(F.data == "main_menu:info")
async def callback_data_info(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text(f"{text_info()}", reply_markup=main_menu_cancel()) # return bot information


@router.callback_query(F.data == "main_menu:cancel")
async def callback_data_main_menu_cancel(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text(f"{text_start(
        name=callback.from_user.first_name, 
        lastname=callback.from_user.last_name)}", reply_markup=main_menu()) # cancel -> return start menu