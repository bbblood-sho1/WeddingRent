import os
from flask import Flask, render_template, request, redirect, url_for, flash
from db import db, get_database_url
from models.user import User, Role
from models.auth import register_user

# Создание приложения Flask
app = Flask(__name__)
# Секретный ключ для защиты сессий Flask
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

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

# Регистрация нового пользователя
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form.get("username", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")

        if len(username) < 3:
            flash("Логин должен содержать минимум 3 символа.")
            return redirect(url_for("register"))

        if len(password) < 12:
            flash("Пароль должен содержать минимум 12 символов.")
            return redirect(url_for("register"))

        success, message = register_user(
            username=username,
            email=email,
            password=password
        )

        flash(message)

        if success:
            return redirect(url_for("register"))

    return render_template("register.html")


# Запуск приложения
if __name__ == "__main__":
    app.run(debug=True)
