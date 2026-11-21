from models.encryption import encrypt_data, decrypt_data

# Тестовая строка
original_text = "Тестовые персональные данные"

# Шифруем текст
encrypted_text = encrypt_data(original_text)

# Расшифровываем результат
decrypted_text = decrypt_data(encrypted_text)

print("Исходный текст:", original_text)
print("Зашифрованный текст:", encrypted_text)
print("Расшифрованный текст:", decrypted_text)

# Проверяем совпадение
if original_text == decrypted_text:
    print("УСПЕХ: шифрование и расшифровка работают!")
else:
    print("ОШИБКА: данные не совпадают!")