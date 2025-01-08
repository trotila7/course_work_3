import logging
from datetime import datetime, timedelta
from typing import Dict, List
import pandas as pd
import requests

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(r'../logs/utils.log', mode='w')
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def get_data_from_xlsx(path: str) -> List[Dict]:
    """Загружает данные из XLSX файла в список словарей."""
    try:
        df = pd.read_excel(path)
        return df.to_dict(orient='records')
    except Exception as e:
        logger.error(f'Ошибка при чтении файла: {e}')
        return []


def filter_transactions_by_date(transactions: List[Dict], input_date_str: str) -> List[Dict]:
    """Фильтрует транзакции по дате."""
    input_date = datetime.strptime(input_date_str, '%d.%m.%Y')
    end_date = input_date + timedelta(days=1)
    start_date = datetime(end_date.year, end_date.month, 1)
    filtered_transactions = [transaction for transaction in transactions
                             if start_date <= datetime.strptime(transaction["Дата операции"],
                                                                '%d.%m.%Y %H:%M:%S') <= end_date]
    return filtered_transactions
