
from flask import Flask, render_template

# Создание приложения Flask
app = Flask(__name__)


# Главная страница
@app.route("/")
def index():
    return render_template("index.html")


# Запуск приложения
if __name__ == "__main__":
    app.run(debug=True)
