from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    external_api_url: str = "https://api.frankfurter.app"
    external_api_key: str | None = None
    database_url: str = "sqlite:///./currency.db"
    cache_ttl_hours: int = 1

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings() 