def text_info() -> str:
    message = """🔎 Augusta Deglava iela 100, Latgales priekšpilsēta, Rīga, LV-1082."""
    return message


def text_sub() -> str:
    message = """💸 Оплату можно произвести в криптовалюте через @CryptoBot или за звёзды."""
    return message


def text_profile(username: str, requests: int, sub_status: str, user_id: int) -> str:
    message = f"""
📊Профиль ⌵
┏ Ваш ник: <code>{username}</code>
┣ Ваш id: <code>{user_id}</code>
┣ Запросы: <code>{requests}</code>
┗ Подписка: <code>{sub_status}</code>"""
    return message


def text_start(name: str, lastname: str) -> str:
    message = f"""👋 Привет, {name} {lastname}! Воспользуйся меню снизу 👇"""
    return message


def text_find_menu() -> str:
    message = ""
    return message