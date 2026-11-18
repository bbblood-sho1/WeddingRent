from flask import Flask

# Создание приложения Flask
app = Flask(__name__)


# Главная страница
@app.route("/")
def index():
    return """
    <h1>WeddingRent</h1>
    <p>Информационная система проката свадебных нарядов</p>
    <p>Сервер успешно запущен!</p>
    """


# Запуск приложения
if __name__ == "__main__":
    app.run(debug=True)