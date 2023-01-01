from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = "127.0.0.1"
    sever_port: int = 8000
    database_url: str = 'postgresql+psycopg2://user:password@hostname/database'


settings = Settings()