import os
from flask import Flask, render_template, request, redirect, url_for, flash
from db import db, get_database_url
from models.user import User, Role
from models.auth import register_user
from flask_login import login_user, logout_user, login_required, current_user
from models.login_manager import login_manager
from models.user import User
from models.auth import verify_password

# Создание приложения Flask
app = Flask(__name__)
# Секретный ключ для защиты сессий Flask
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

# Настройка подключения к PostgreSQL
app.config["SQLALCHEMY_DATABASE_URI"] = get_database_url()
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Подключение SQLAlchemy к приложению
db.init_app(app)
# Подключение Flask-Login
login_manager.init_app(app)


# Загрузка пользователя из базы данных по его ID
@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


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

# Вход пользователя в систему
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        # Поиск пользователя по логину
        user = User.query.filter_by(username=username).first()

        # Проверка существования пользователя и пароля
        if user and user.is_active and verify_password(
            password,
            user.password_hash
        ):
            login_user(user)

            flash("Вы успешно вошли в систему.")
            return redirect(url_for("index"))

        flash("Неверный логин или пароль.")

    return render_template("login.html")

# Выход пользователя из системы
@app.route("/logout")
@login_required
def logout():

    logout_user()

    flash("Вы вышли из системы.")
    return redirect(url_for("index"))



# Запуск приложения
if __name__ == "__main__":
    app.run(debug=True)
