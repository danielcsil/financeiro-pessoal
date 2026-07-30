from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str
    app_env: str
    app_debug: bool

    postgres_host: str
    postgres_port: int
    postgres_user: str
    postgres_password: str
    postgres_db: str

    secret_key: str
    access_token_expire_minutes: int
    algorithm: str

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+psycopg://"
            f"{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}"
            f"/{self.postgres_db}"
        )

    class Config:
        env_file = ".env"


settings = Settings()