from typing import List

from pydantic_settings import BaseSettings

from pathlib import Path


BASE_DIR = Path(__file__).parent.parent

class Settings(BaseSettings):
    bot_token: str

    class Config:
        env_file = BASE_DIR / ".env" # .env file
        env_file_encoding = "utf-8"
        arbitrary_types_allowed = True

settings = Settings()