from aiogram import types, Router, F

from callbacks import text_info, text_sub

router = Router()

@router.callback_query(F.data == "main_menu:profile")
async def callback_data_profile(callback: types.CallbackQuery) -> None:
    await callback.answer("soon...") # return profile


@router.callback_query(F.data == "main_menu:buy_sub")
async def callback_data_buy_sub(callback: types.CallbackQuery) -> None:
    await callback.answer(f"{text_sub()}") # return subscription menu


@router.callback_query(F.data == "main_menu:info")
async def callback_data_info(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text(f"{text_info()}") # return bot information