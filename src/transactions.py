from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
transactions_csv = BASE_DIR / "data" / "transactions_csv.csv"
transactions_xlsx = BASE_DIR / "data" / "transactions_excel.xlsx"


def load_transactions_сsv(file_path_csv: Path, sep=";") -> list:
    """
    Принимает на вход путь до csv-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """

    try:
        csv_data = pd.read_csv(file_path_csv, sep=sep)
        return csv_data.to_dict(orient="records")

    except pd.errors.EmptyDataError:
        return []
    except Exception:
        return []


transactions_csv = load_transactions_сsv(transactions_csv)
print(transactions_csv)


def load_transactions_xlsx(file_path_xlsx: Path) -> list:
    """
    Принимает на вход путь до xlsx-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """

    try:
        excel_data = pd.read_excel(file_path_xlsx, sheet_name=0)
        return excel_data.to_dict(orient="records")

    except pd.errors.EmptyDataError:
        return []
    except Exception:
        return []


transactions_xlsx = load_transactions_xlsx(transactions_xlsx)
print(transactions_xlsx)
