def text_info() -> str:
    message = """🔎 Augusta Deglava iela 100, Latgales priekšpilsēta, Rīga, LV-1082."""
    return message

def text_sub() -> str:
    message = """💸 Оплату можно произвести в криптовалюте через @CryptoBot или за звёзды."""
    return message

def text_profile(name: str, requests: int, sub_status: str, id: int) -> str:
    message = f"""
📊Профиль 👇 
    
╔ Name: {name} 
╠ Запросы: {requests}
╠ Sub: {sub_status}
╚ ID: {id}

    """
    return message

def text_start(name: str, lastname: str) -> str:
    message = f"""👋 Привет, {name} {lastname}! Воспользуйся меню снизу 👇"""
    return message

# def text_cancel() -> str:
#     message = """"""
#     return message
