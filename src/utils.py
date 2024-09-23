import json
import os

def load_transactions(file_path):
    if not os.path.exists(file_path):
        return []

    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            return []

    if isinstance(data, list):
        return data
    else:
        return []

transactions = load_transactions('data/operations.json')
print(transactions)

# Импортируем необходимые модули: мы используем json для работы с JSON-файлом и os для проверки существования файла.
# Функция load_transactions:
# Аргумент file_path принимает путь к JSON-файлу.
# Проверяем, существует ли файл. Если нет, возвращаем пустой список.
# Если файл существует, открываем его и пытаемся загрузить данные с помощью json.load().
# Обрабатываем возможные ошибки при чтении JSON с помощью try-except, чтобы избежать исключения, если файл не является корректным JSON.
# Проверяем, является ли загруженные данные списком. Если да, возвращаем его, иначе возвращаем пустой список.