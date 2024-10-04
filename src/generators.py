from typing import Generator, Iterator


def filter_by_currency(transactions: list, key: str = "USD") -> Iterator[list]:
    """
    Принимает на вход список словарей, представляющих транзакции.
    Функция должна возвращать итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD).
    """

    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == key:
            yield transaction


#
# try:
#     transactions = [{
#           "id": 939719570,
#           "state": "EXECUTED",
#           "date": "2018-06-30T02:08:58.425572",
#           "operationAmount": {
#               "amount": "9824.07",
#               "currency": {
#                   "name": "USD",
#                   "code": "USD"
#               }
#           },
#           "description": "Перевод организации",
#           "from": "Счет 75106830613657916952",
#           "to": "Счет 11776614605963066702"
#       },
#       {
#           "id": 142264268,
#               "state": "EXECUTED",
#               "date": "2019-04-04T23:20:05.206878",
#               "operationAmount": {
#                   "amount": "79114.93",
#                   "currency": {
#                       "name": "USD",
#                       "code": "USD"
#                   }
#               },
#               "description": "Перевод со счета на счет",
#               "from": "Счет 19708645243227258542",
#               "to": "Счет 75651667383060284188"
#        },
#         {
#             "id": 142264268,
#             "state": "EXECUTED",
#             "date": "2019-04-04T23:20:05.206878",
#             "operationAmount": {
#                 "amount": "79114.93",
#                 "currency": {
#                     "name": "EURO",
#                     "code": "EURO"
#                 }
#             },
#             "description": "Перевод со счета на счет",
#             "from": "Счет 19708645243227258542",
#             "to": "Счет 75651667383060284188"
#         },
#         {
#             "id": 142264268,
#             "state": "EXECUTED",
#             "date": "2019-04-04T23:20:05.206878",
#             "operationAmount": {
#                 "amount": "79114.93",
#                 "currency": {}
#             },
#             "description": "Перевод со счета на счет",
#             "from": "Счет 19708645243227258542",
#             "to": "Счет 75651667383060284188"
#         },
#         {},
#         {
#             "id": 142264268,
#             "state": "EXECUTED",
#             "date": "2019-05-05T23:20:05.206878",
#             "operationAmount": {
#                 "amount": "79114.93",
#                 "currency": {
#                     "name": "USD",
#                     "code": "USD"
#                 }
#             },
#             "description": "Перевод со счета на счет",
#             "from": "Счет 19708645243227258542",
#             "to": "Счет 75651667383060284188"
#         }
#     ]
#
#     usd_transactions = filter_by_currency(transactions, 'EURO')
#
#     for _ in range(2):
# #         print(next(usd_transactions))
# #
# except StopIteration:
#         print('Больше нет операций в заданной валюте')


def transaction_descriptions(transactions: list) -> Generator[list, list, None]:
    """
    Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди
    """

    for transaction in transactions:
        if transaction.get("description"):
            yield transaction.get("description")


# descriptions = transaction_descriptions(transactions)
#
# for _ in range(4):
#     print(next(descriptions))


def card_number_generator(start: int, stop: int) -> Generator[str, str, None]:
    """
    Выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    Генератор должен принимать начальное и конечное значения для генерации диапазона номеров.
    """
    # Генерируем номера карт
    if start < 1 or stop >= 10**16:
        return print("Неверно введенные данные")
    else:
        for num in range(start, stop + 1):
            # Форматируем номер карты в нужный формат XXXX XXXX XXXX XXXX

            formatted_number = f"{num:016}"

            yield f"{formatted_number[:4]} {formatted_number[4:8]} {formatted_number[8:12]} {formatted_number[12:]}"


# for card in card_number_generator(0, 1):
#     print(card)
