from aiogram import types, Router, F

from callbacks import text_info, text_sub, text_start, text_profile
from callbacks import main_menu_cancel, main_menu
from other.texts import text_find_menu

from bot.other.texts import text_profile

router = Router()

@router.callback_query(F.data == "main_menu:profile")
async def callback_data_profile(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text(F"{text_profile()}", reply_markup=main_menu_cancel()) # return profile

    await callback.message.edit_text(f"{text_profile(
        username=callback.from_user.first_name,
        requests=1,
        sub_status="активна до ...",
        user_id=callback.from_user.id
    )}", reply_markup=main_menu_cancel()) # return profile



@router.callback_query(F.data == "main_menu:buy_sub")
async def callback_data_buy_sub(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text(f"{text_sub()}", reply_markup=main_menu_cancel()) # return subscription menu


@router.callback_query(F.data == "main_menu:info")
async def callback_data_info(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text(f"{text_info()}", reply_markup=main_menu_cancel()) # return bot information


@router.callback_query(F.data == "main_menu:find_menu")
async def callback_data_find_menu(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text(f"{text_find_menu()}", reply_markup=)


@router.callback_query(F.data == "main_menu:cancel")
async def callback_data_main_menu_cancel(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text(f"{text_start(
        name=callback.from_user.first_name, 
        lastname=callback.from_user.last_name)}", reply_markup=main_menu()) # cancel -> return start menu