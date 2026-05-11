from aiogram import types, Router, F

from callbacks import admin_menu, admin_menu_cancel

router = Router()


@router.callback_query(F.data == "admin_menu:broadcast") # broadcast
async def callback_data_broadcast(callback: types.CallbackQuery) -> None:
    # user_text =
    await callback.message.edit_text(text="Введите сообщение для рассылки ниже:",
                                     reply_markup=admin_menu_cancel())
    # TODO: Доделать админку и добавить state (ожидания)
