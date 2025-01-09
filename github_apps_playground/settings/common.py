from pydantic_settings import BaseSettings, SettingsConfigDict


class CommonSettings(BaseSettings):
    common_version: str
    common_log_level: str

    model_config = SettingsConfigDict(env_file=".env")
