import functools
import json
import logging
from datetime import datetime, timedelta
import pandas as pd

# Логирование
logger = logging.getLogger("reports")
file_handler = logging.FileHandler('../logs/reports.log', mode='w')
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def report_to_file(func):
    """Записывает результат работы функции в файл"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open("report.txt", "w") as file:
            file.write(str(result))
        return result

    return wrapper


@report_to_file
def spending_by_category(transactions: pd.DataFrame, category: str, date=None) -> str:
    # Логика для расчета трат по категории за последние 3 месяца
    pass


@report_to_file
def spending_by_weekday(transactions: pd.DataFrame, date=None) -> str:
    # Логика для расчета трат по дням недели
    pass


@report_to_file
def spending_by_workday(transactions: pd.DataFrame, date=None) -> str:
    # Логика для расчета трат по рабочим/выходным дням
    pass
