from typing import Optional

def username_is_none(username: Optional[str]) -> str:
    return username or "Нет username"

def first_name_is_none(first_name: Optional[str]) -> str:
    return first_name or ""

def last_name_is_none(last_name: Optional[str]) -> str:
    return last_name or ""