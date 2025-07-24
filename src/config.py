from typing import Optional
from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    VERSION: str = "1.0.0"
    DEBUG: bool
    YANDEX_IAM_KEY: SecretStr
    YANDEX_FOLDER_ID: Optional[SecretStr] = None

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

    @property
    def STT_URL_V1(self):
        return f"https://stt.api.cloud.yandex.net/speech/v1/stt:recognize"


settings = Settings()
