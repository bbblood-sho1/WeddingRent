import os

from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()


def get_encryption_key():
    key = os.getenv("ENCRYPTION_KEY")

    if not key:
        raise ValueError(
            "Ключ шифрования ENCRYPTION_KEY не найден в .env"
        )

    return key.encode()


def encrypt_data(data):
    if not data:
        return data

    fernet = Fernet(get_encryption_key())
    encrypted_data = fernet.encrypt(data.encode())

    return encrypted_data.decode()


def decrypt_data(encrypted_data):
    if not encrypted_data:
        return encrypted_data

    fernet = Fernet(get_encryption_key())
    decrypted_data = fernet.decrypt(encrypted_data.encode())

    return decrypted_data.decode()