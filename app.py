
from flask import Flask, render_template
from db import db, get_database_url

# Создание приложения Flask
app = Flask(__name__)

# Настройка подключения к PostgreSQL
app.config["SQLALCHEMY_DATABASE_URI"] = get_database_url()
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Подключение SQLAlchemy к приложению
db.init_app(app)


# Главная страница
@app.route("/")
def index():
    return render_template("index.html")


# Проверка подключения к базе данных
@app.route("/db-check")
def db_check():
    try:
        with db.engine.connect() as connection:
            connection.exec_driver_sql("SELECT 1")

        return "Подключение к PostgreSQL успешно!"

    except Exception:
        app.logger.exception("Ошибка подключения к базе данных")
        return "Не удалось подключиться к базе данных.", 500


# Запуск приложения
if __name__ == "__main__":
    app.run(debug=True)
