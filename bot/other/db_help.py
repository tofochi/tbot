from datetime import datetime
from typing import Optional


def db_date_to_iso_format(date: Optional[datetime]) -> Optional[str]:
    if date is not None:
        return date.isoformat()
    else:
        return None


def db_iso_format_to_date(date_iso_format: Optional[str]) -> Optional[datetime]:
    if date_iso_format is not None:
        return datetime.fromisoformat(date_iso_format)
    else:
        return None

def subscription_format(bad_format: Optional[int]) -> Optional[str]:
    if bad_format == 0:
        return "Неактивна"
    else:
        return "Активна"