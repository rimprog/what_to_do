from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Настройки приложения"""

    # Настройки прокси и API
    PROXY: str = None  # По умолчанию None, если прокси не используется
    OPEN_AI_API_KEY: str
    DOMAIN_NAME: str
    DEVELOPER_EMAIL: str

    # Путь к файлу настроек
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


# Инициализация настроек
settings = Settings()
