from flask_login import current_user
from models.audit import AuditLog
from db import db


def log_action(action, entity_type=None, entity_id=None, details=None):
    """Запись действия пользователя в журнал безопасности."""

    user_id = None

    if current_user.is_authenticated:
        user_id = current_user.id

    log = AuditLog(
        user_id=user_id,
        action=action,
        entity_type=entity_type,
        entity_id=entity_id,
        details=details
    )

    db.session.add(log)
    db.session.commit()
