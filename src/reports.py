import functools
import json
import logging
from datetime import datetime, timedelta

import pandas as pd

logger = logging.getLogger("reports")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(r'../logs/reports.log', mode='w')
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def report_to_file_default(func):
    """Записывает в файл результат, который возвращает функция, формирующая отчет."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open("function_operation_report.txt", "w") as file:
            file.write(str(result))
        logger.info(f'Записан результат работы функции {func}')
        return result

    return wrapper


@report_to_file_default
def spending_by_category(transactions: pd.DataFrame, category: str, date=None) -> str:
    """Функция возвращает траты по заданной категории за последние три месяца."""
    try:
        transactions['Дата операции'] = pd.to_datetime(transactions['Дата операции'], format='%d.%m.%Y %H:%M:%S')
        if date is None:
            date = datetime.now()
        else:
            date = datetime.strptime(date, '%Y.%m.%d')
        start_date = date - timedelta(days=date.day - 1) - timedelta(days=3 * 30)
        filtered_transactions = transactions[
            (transactions['Дата операции'] >= start_date) & (transactions['Дата операции'] <= date) & (
                        transactions['Категория'] == category)]
        result = filtered_transactions.to_dict(orient='records')
        for record in result:
            record['Дата операции'] = record['Дата операции'].strftime('%d.%m.%Y %H:%M:%S')
        formatted_result = json.dumps(result, ensure_ascii=False, indent=4)
        logger.info(f'Траты за последние три месяца от {date} по категории {category}')
        return formatted_result
    except Exception as e:
        logger.error(f'Ошибка: {e}')
        return ""
