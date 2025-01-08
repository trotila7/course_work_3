import os
import logging
from datetime import datetime, timedelta
import pandas as pd

# Создание директории для логов, если она не существует
log_dir = "../logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Настройка логирования
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(os.path.join(log_dir, "utils.log"), mode='w')
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def get_data_from_xlsx(path: str):
    """Функция для чтения данных из xlsx файла"""
    try:
        df = pd.read_excel(path)
        logger.info('Файл успешно загружен')
        return df.to_dict(orient='records')
    except Exception as e:
        logger.error(f'Ошибка при загрузке данных из файла: {e}')
        return []


def filter_transactions_by_date(transactions, input_date_str):
    """Функция фильтрует транзакции по заданной дате"""
    input_date = datetime.strptime(input_date_str, '%d.%m.%Y')
    end_date = input_date + timedelta(days=1)
    start_date = datetime(end_date.year, end_date.month, 1)

    def parse_date(date_str):
        """Функция для преобразования строки в дату"""
        return datetime.strptime(date_str, '%d.%m.%Y %H:%M:%S')

    filtered_transactions = [transaction for transaction in transactions
                             if start_date <= parse_date(transaction["Дата операции"]) <= end_date]
    logger.info(f'Фильтрация транзакций с {start_date} до {end_date}')
    return filtered_transactions
