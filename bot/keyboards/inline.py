from aiogram.utils.keyboard import InlineKeyboardBuilder


def main_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="💼 Профиль", callback_data="main_menu:profile")
    builder.button(text="📕 Информация", callback_data="main_menu:info")
    builder.button(text="📲 Меню", callback_data="main_menu:find_menu")
    builder.button(text="💳 Купить подписку", callback_data="main_menu:buy_sub")
    builder.adjust(2, 1, 1)
    return builder.as_markup()

def main_menu_cancel():
    builder = InlineKeyboardBuilder()
    builder.button(text="↩ Отмена", callback_data="main_menu:cancel")
    builder.adjust(1)
    return builder.as_markup()
