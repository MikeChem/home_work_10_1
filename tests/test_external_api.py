from unittest.mock import patch

import pytest

from src.external_api import conversion_func


@pytest.fixture
def transaction_rub():
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


transaction_usd = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "USD"}},
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589",
}


# Тест на корректную работу функции когда на вход подается транзакция в валюте RUB
def test_conversion_func_rub(transaction_rub):
    assert conversion_func(transaction_rub) == 31957.58


# Тест на корректную работу функции когда на вход подается транзакция в валюте USD
@patch("requests.request")
def test_conversion_func_usd(mock_get):
    mock_get.return_value.json.return_value = {"result": 2947786.162003}
    assert conversion_func(transaction_usd) == 0.0
    mock_get.assert_called()
