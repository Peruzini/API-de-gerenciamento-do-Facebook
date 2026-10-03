from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_env: str = "development"
    app_host: str = "0.0.0.0"
    app_port: int = 8000

    database_url: str

    meta_app_id: str
    meta_app_secret: str
    meta_verify_token: str
    meta_graph_version: str
    meta_graph_base_url: str = "https://graph.facebook.com"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
