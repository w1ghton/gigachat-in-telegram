from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    model_config = {
        "env_file": ".env",
        "case_sensitive": False,
    }
    telegram_bot_token: str = Field(pattern=r"[0-9]{10}\:[\S]{35}")
    gigachat_api_key: str = Field(pattern=r"[\S]{98}\={2}")
