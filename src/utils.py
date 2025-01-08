import pandas as pd
from datetime import datetime, timedelta


def get_data_from_xlsx(path: str) -> list:
    """Чтение транзакций из файла Excel"""
    try:
        df = pd.read_excel(path)
        return df.to_dict(orient='records')
    except Exception as e:
        print(f'Ошибка: {e}')
        return []


def filter_transactions_by_date(transactions: list, input_date_str: str) -> list:
    """Фильтрация транзакций по дате"""
    input_date = datetime.strptime(input_date_str, '%d.%m.%Y')
    end_date = input_date + timedelta(days=1)
    start_date = datetime(end_date.year, end_date.month, 1)
    filtered_transactions = [t for t in transactions if
                             start_date <= datetime.strptime(t["Дата операции"], '%d.%m.%Y %H:%M:%S') <= end_date]
    return filtered_transactions
