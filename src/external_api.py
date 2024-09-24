import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
payload = {}

headers = {"apikey": API_KEY}


def conversion_func(transaction):
    """
    Принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях.
    Если транзакция была в USD или EUR, происходит обращение к внешнему API
    для получения текущего курса валют и конвертации суммы операции в рубли.
    """

    try:
        curr_code_to = "RUB"
        currency = transaction["operationAmount"]["currency"]["code"]
        amount = transaction["operationAmount"]["amount"]
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={curr_code_to}&from={currency}&amount={amount}"

        if currency not in "RUB":
            response = requests.request("GET", url, headers=headers, data=payload)

            if response.status_code == 200:
                result = response.json()["result"]
                return float(result)
            else:
                return 0.0
        else:
            return float(amount)
    except KeyError:
        return "Транзакция не найдена"


# from src.utils import load_transactions
#
# # Загрузите транзакции из JSON-файла
# transactions = load_transactions("../data/operations.json")
#
# # Обрабатываем каждую транзакцию
# for transaction in transactions:
#     amount_in_rub = conversion_func(transaction)
#     print(f"Transaction amount in RUB: {amount_in_rub}")
