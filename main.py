from src.transactions import load_transactions_сsv, load_transactions_xlsx
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
transactions_csv = BASE_DIR / 'data' / 'transactions_csv.csv'
transactions_xlsx = BASE_DIR / 'data' / 'transactions_excel.xlsx'

transactions_csv = load_transactions_сsv(transactions_csv)
print(transactions_csv)

transactions_xlsx = load_transactions_xlsx(transactions_xlsx)
print(transactions_xlsx)
