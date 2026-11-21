from app import app

app.config["TESTING"] = True
app.config["WTF_CSRF_ENABLED"] = True

with app.test_client() as client:
    response = client.post(
        "/login",
        data={
            "username": "test_user",
            "password": "test_password"
        }
    )

    print("Код ответа:", response.status_code)

    if response.status_code == 400:
        print("УСПЕХ: запрос без CSRF-токена заблокирован.")
    else:
        print("ПРОВЕРЬТЕ: ожидался код 400.")