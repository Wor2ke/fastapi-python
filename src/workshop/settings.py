from pydantic import BaseSettings
import psycopg2


class Settings(BaseSettings):
    server_host: str = "127.0.0.1"
    sever_port: int = 8000
    database_url: str = 'postgresql+psycopg2://postgres:root@localhost/workshop'


settings = Settings()