from pydantic import BaseSettings


class Settings(BaseSettings):
    USER_ID: str
    USER_SECRET: str

    DATABASE_URL: str
    GITHUB_USER: str
    GITHUB_TOKEN: str


settings = Settings()
