
import os

from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

# Загрузка переменных из файла .env
load_dotenv()

# Создание объекта базы данных
db = SQLAlchemy()


def get_database_url():
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    name = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")

    return (
        f"postgresql+psycopg2://{user}:{password}"
        f"@{host}:{port}/{name}"
    )
