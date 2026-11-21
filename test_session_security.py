from app import app

with app.test_client() as client:
    print("Проверка настроек безопасности сессии:")

    print(
        "HttpOnly:",
        app.config["SESSION_COOKIE_HTTPONLY"]
    )

    print(
        "SameSite:",
        app.config["SESSION_COOKIE_SAMESITE"]
    )

    print(
        "Secure:",
        app.config["SESSION_COOKIE_SECURE"]
    )

    assert app.config["SESSION_COOKIE_HTTPONLY"] is True
    assert app.config["SESSION_COOKIE_SAMESITE"] == "Lax"
    assert app.config["SESSION_COOKIE_SECURE"] is False

    print("УСПЕХ: настройки безопасности применены!")