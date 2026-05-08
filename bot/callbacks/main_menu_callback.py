from aiogram import types, Router, F

from callbacks import (text_main_menu_info,
                       text_main_menu_sub,
                       text_main_menu_profile,
                       text_find_menu,
                       )
from callbacks import main_menu, main_menu_cancel
from callbacks import find_menu

router = Router()

@router.callback_query(F.data == "main_menu:profile")
async def callback_data_profile(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text(f"{text_main_menu_profile(
        username=callback.from_user.first_name,
        requests=1,
        sub_status="активна до ...",
        user_id=callback.from_user.id
    )}", reply_markup=main_menu_cancel()) # return profile


@router.callback_query(F.data == "main_menu:buy_sub")
async def callback_data_buy_sub(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text(text_main_menu_sub(), reply_markup=main_menu_cancel()) # return subscription menu


@router.callback_query(F.data == "main_menu:info")
async def callback_data_info(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text(text_main_menu_info(), reply_markup=main_menu_cancel()) # return bot information


@router.callback_query(F.data == "main_menu:send_message_to_support")
async def callback_data_send_to_support(callback: types.CallbackQuery) -> None:
    await callback.message.answer(reply_markup=main_menu_cancel()) # return support info


@router.callback_query(F.data == "main_menu:find_menu")
async def callback_data_find_menu(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text(text_find_menu(), reply_markup=find_menu()) # main_menu:find_menu -> find_menu:...