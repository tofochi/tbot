from aiogram.utils.keyboard import InlineKeyboardBuilder


def main_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="💼 Профиль", callback_data="main_menu:profile")
    builder.button(text="📕 Информация", callback_data="main_menu:info")
    builder.button(text="💳 Купить подписку", callback_data="main_menu:buy_sub")
    builder.button(text="🔍 Google Dorks", callback_data="main_menu:google_dorks")
    builder.adjust(2, 1)
    return builder.as_markup()
