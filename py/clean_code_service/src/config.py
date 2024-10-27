from pydantic_settings import BaseSettings


class AppConfig(BaseSettings, case_sensitive=False):

    host: str
    port: int
    reload_after_change: bool

    class Config:
        """Config Settings."""

        env_file = '.env'
        env_file_encoding = 'utf-8'
