from pydantic import BaseSettings

from src.internal.utils.singleton import singleton


@singleton
class ConverterSettings(BaseSettings):
    """Basic settings 4 redis database."""

    secret_key: str

    class Config:
        """Config 4 Redis Settings."""

        env_file = ".env"
        env_file_encoding = "utf-8"


settings = ConverterSettings()
