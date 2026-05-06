from typing import List

from pydantic_settings import BaseSettings

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent


class Settings(BaseSettings):
    bot_token: str

    class Config:
        env_file = BASE_DIR / ".env"  # .env file
        env_file_encoding = "utf-8"   # format
        extra = "ignore"
        arbitrary_types_allowed = True

def check_settings() -> None:
    settings = Settings()
    if settings.bot_token is None:
        print("Error. Token not set")
    else:
        print("Good. Token set")

def load_settings() -> Settings:
    return Settings()