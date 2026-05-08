def text_main_menu_info() -> str:
    message = """
🔎 python, aiogram 3.x
🥩 Augusta Deglava iela 100, Latgales priekšpilsēta, Rīga, LV-1082."""
    return message


def text_main_menu_sub() -> str:
    message = """💸 Оплату можно произвести в криптовалюте через @CryptoBot или за звёзды."""
    return message


def text_main_menu_profile(username: str, requests: int, sub_status: str, user_id: int) -> str:
    message = f"""
📊Профиль ⌵

┏ Ваш ник: <code>{username}</code>
┣ Ваш id: <code>{user_id}</code>
┣ Запросы: <code>{requests}</code>
┗ Подписка: <code>{sub_status}</code>"""
    return message


def text_main_menu_start(name: str, lastname: str | None) -> str:
    message = f"""👋 Привет, {name} {lastname}! Воспользуйся меню снизу 👇"""
    return message


def text_main_menu_support() -> str:
    message = """Пиши создателю бота Фабрика Иллюзий""" # добавить юз или канал
    return message


def text_find_menu() -> str:
    message = f"""Выбери действие ниже 👇"""
    return message


def text_find_menu_osint_search() -> str:
    message = """таргет осинт"""
    return message

def text_find_menu_database_search() -> str:
    message = """таргет дб"""
    return message

def text_find_menu_send_mail() -> str:
    message = """таргет маил"""
    return message

def text_find_menu_generate_username() -> str:
    message = """таргет юзернейм"""
    return message