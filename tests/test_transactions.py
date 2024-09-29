from unittest.mock import patch

import pandas as pd

from src.transactions import load_transactions_xlsx, load_transactions_сsv, transactions_csv, transactions_xlsx


@patch("src.transactions.pd.read_csv")
def test_valid_file_csv(mock_read, test_df):
    mock_read.return_value = test_df
    result = load_transactions_сsv(transactions_csv)
    assert result == test_df.to_dict(orient="records")


# Тест на пустой файл
@patch("src.transactions.pd.read_csv")
def test_empty_file_csv(mock_file):
    mock_file.side_effect = pd.errors.EmptyDataError
    result = load_transactions_сsv(transactions_csv)
    assert result == []


# Тест на некорректный тип данных(не список)
@patch("builtins.open", side_effect=Exception)
def test_error_csv(mock_file):
    result = load_transactions_сsv(transactions_csv)
    assert result == []


@patch("src.transactions.pd.read_excel")
def test_valid_file_xlsx(mock_read, test_df):
    mock_read.return_value = test_df
    result = load_transactions_xlsx(transactions_xlsx)
    assert result == test_df.to_dict(orient="records")


# Тест на пустой файл
@patch("src.transactions.pd.read_excel")
def test_empty_file_xlsx(mock_file):
    mock_file.side_effect = pd.errors.EmptyDataError
    result = load_transactions_xlsx(transactions_xlsx)
    assert result == []


# Тест на некорректный тип данных(не список)
@patch("builtins.open", side_effect=Exception)
def test_not_list_csv(mock_file):
    result = load_transactions_xlsx(transactions_xlsx)
    assert result == []
