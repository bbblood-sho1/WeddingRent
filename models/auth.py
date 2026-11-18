
from werkzeug.security import generate_password_hash, check_password_hash


def hash_password(password):
    """Создание безопасного хеша пароля."""
    return generate_password_hash(
        password,
        method="scrypt"
    )


def verify_password(password, password_hash):
    """Проверка введённого пароля."""
    return check_password_hash(password_hash, password)

from db import db
from models.user import User, Role


def register_user(username, email, password, role_name="client"):
    """Регистрация нового пользователя."""

    # Проверяем, существует ли логин
    existing_username = User.query.filter_by(
        username=username
    ).first()

    if existing_username:
        return False, "Такой логин уже занят."

    # Проверяем, существует ли электронная почта
    existing_email = User.query.filter_by(
        email=email
    ).first()

    if existing_email:
        return False, "Такая электронная почта уже зарегистрирована."

    # Находим роль пользователя
    role = Role.query.filter_by(name=role_name).first()

    if role is None:
        return False, "Указанная роль не найдена."

    # Создаём пользователя
    user = User(
        username=username,
        email=email,
        password_hash=hash_password(password),
        role_id=role.id
    )

    # Сохраняем пользователя
    try:
        db.session.add(user)
        db.session.commit()

        return True, "Пользователь успешно зарегистрирован."

    except Exception:
        db.session.rollback()
        raise
