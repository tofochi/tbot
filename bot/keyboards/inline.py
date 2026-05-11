from aiogram.utils.keyboard import InlineKeyboardBuilder


def main_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="💼 Профиль", callback_data="main_menu:profile")
    builder.button(text="📲 Меню", callback_data="main_menu:find_menu")
    builder.button(text="📕 Информация", callback_data="main_menu:info")
    builder.button(text="💳 Купить подписку", callback_data="main_menu:buy_sub")
    builder.button(text="🆘 Поддержка", callback_data="main_menu:send_message_to_support", url="tg://user?id=8433550795")
    builder.adjust(2, 2, 1)
    return builder.as_markup()

def main_menu_cancel():
    builder = InlineKeyboardBuilder()
    builder.button(text="↩ Отмена", callback_data="main_menu:cancel")
    builder.adjust(1)
    return builder.as_markup()


def find_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="🔍 OSINT поиск", callback_data="find_menu:osint_search")
    builder.button(text="📁 БД поиск", callback_data="find_menu:database_search")
    builder.button(text="📥 Отправить письмо", callback_data="find_menu:send_mail")
    builder.button(text="🥷 Генерация username", callback_data="find_menu:generate_username")
    builder.button(text="↩ Отмена", callback_data="find_menu:cancel_to_main_menu")
    builder.adjust(2, 2, 1)
    return builder.as_markup()

def find_menu_cancel():
    builder = InlineKeyboardBuilder()
    builder.button(text="↩ Отмена", callback_data="find_menu:cancel_to_find_menu")
    builder.adjust(1)
    return builder.as_markup()


def admin_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="Сделать рассылку", callback_data="admin_menu:broadcast")
    builder.button(text="Добавить подписку", callback_data="admin_menu:add_sub")
    builder.button(text="Добавить запросов", callback_data="admin_menu:add_requests")
    builder.button(text="История поиска", callback_data="admin_menu:check_history_search")
    builder.button(text="Список пользователей", callback_data="admin_menu:check_list_users")
    builder.button(text="Статистика пользователя", callback_data="admin_menu:check_statistics_user")
    builder.adjust(2, 2, 1, 1)
    return builder.as_markup()


def admin_menu_cancel():
    builder = InlineKeyboardBuilder()
    builder.button(text="↩ Отмена", callback_data="admin_menu:cancel")
    builder.adjust(1)
    return builder.as_markup()




# def support_menu():
#     builder = InlineKeyboardBuilder()
#     builder.button(text="Написать поддержке", callback_data="support_menu:send_message_to_support")
#     builder.button(text="↩ Отмена", callback_data="support_menu:cancel")
#     builder.adjust(1, 1)
#     return builder.as_markup()
