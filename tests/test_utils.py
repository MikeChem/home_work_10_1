from unittest.mock import mock_open, patch

from src.utils import load_transactions_json


# Тест на корректный файл с транзакциями
@patch("builtins.open", new_callable=mock_open, read_data='[{"amount": 100, "currency": "USD"}]')
def test_valid_file(mock_file):
    transaction = load_transactions_json("../data/operations.json")
    assert transaction == [{"amount": 100, "currency": "USD"}]


# Тест на пустой файл
@patch("builtins.open", new_callable=mock_open, read_data="")
def test_empty_file(mock_file):
    transaction = load_transactions_json("../data/operations.json")
    assert transaction == []


# Тест на некорректный тип данных(не список)
@patch("builtins.open", new_callable=mock_open, read_data='{"amount": 100, "currency": "USD"}')
def test_not_list(mock_file):
    transaction = load_transactions_json("../data/operations.json")
    assert transaction == []


# Если файл не найден
@patch("builtins.open", side_effect=FileNotFoundError)
def test_file_not_found(mock_file):
    transaction = load_transactions_json("../data/operations.json")
    assert transaction == []
