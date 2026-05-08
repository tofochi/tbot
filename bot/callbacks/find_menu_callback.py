from aiogram import types, Router, F

from callbacks import (text_find_menu,
                       text_find_menu_osint_search,
                       text_find_menu_database_search,
                       text_find_menu_send_mail,
                       text_find_menu_generate_username)

from callbacks import find_menu, find_menu_cancel

from callbacks import (
    text_main_menu_start,
    main_menu,
)

router = Router()


@router.callback_query(F.data == "find_menu:osint_search")
async def callback_data_osint_search(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text(text=text_find_menu_osint_search(), reply_markup=find_menu_cancel())


@router.callback_query(F.data == "find_menu:database_search")
async def callback_data_osint_search(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text(text=text_find_menu_database_search(), reply_markup=find_menu_cancel())


@router.callback_query(F.data == "find_menu:send_mail")
async def callback_data_osint_search(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text(text=text_find_menu_database_search(), reply_markup=find_menu_cancel())


@router.callback_query(F.data == "find_menu:generate_username")
async def callback_data_osint_search(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text(text=text_find_menu_database_search(), reply_markup=find_menu_cancel()) # TODO: часть киселя