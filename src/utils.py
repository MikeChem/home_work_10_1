import json
import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
transactions_json = BASE_DIR / "data" / "operations.json"


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="./logs/utils.log",
    filemode="w",
)

logger = logging.getLogger("utils")


def load_transactions_json(file_path):
    """
    Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """

    try:
        logger.info("Открытие файла по указанному пути")
        with open(file_path, "r", encoding="utf-8") as file:
            try:
                logger.info("Преобразование json-данных из файла")
                data = json.load(file)
                if isinstance(data, list):
                    return data
                else:
                    return []
            except json.JSONDecodeError:
                logger.warning("Ошибка: некорректные данные")
                return []
    except FileNotFoundError:
        logger.error("Ошибка: Некорректный путь к файлу, либо файл отсутствует")
        return []


transactions_json = load_transactions_json(transactions_json)

# print(transactions_json)
