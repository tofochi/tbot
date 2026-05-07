from aiogram import types, Router, F


router = Router()


@router.callback_query(F.data == "find_menu:")
async def callback_data_profile(callback: types.CallbackQuery) -> None:
    pass