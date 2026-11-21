
from flask_login import LoginManager

# Создание менеджера авторизации
login_manager = LoginManager()

# Страница, на которую перенаправляется
# неавторизованный пользователь
login_manager.login_view = "login"

# Сообщение для пользователя
login_manager.login_message = "Сначала необходимо войти в систему."

# Язык сообщения
login_manager.login_message_category = "warning"
