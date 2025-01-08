import json
import logging
from datetime import datetime
from typing import Dict, List

logger = logging.getLogger("services")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(r'../logs/services.log', mode='w')
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def analyze_cashback(transactions: List[Dict], year: int, month: int) -> str:
    """Считает сумму кэшбека по категориям."""
    try:
        cashback_analysis: Dict = {}
        for transaction in transactions:
            transaction_date = datetime.strptime(transaction["Дата операции"], '%d.%m.%Y %H:%M:%S')
            if transaction_date.year == year and transaction_date.month == month:
                category = transaction["Категория"]
                amount = transaction["Сумма операции"]
                if amount < 0:
                    cashback_value = transaction["Кэшбэк"]
                    cashback = cashback_value if cashback_value else round(amount * -0.01, 5)
                    cashback_analysis[category] = cashback_analysis.get(category, 0) + cashback
        return json.dumps(cashback_analysis, ensure_ascii=False, indent=4)
    except Exception as e:
        logger.error(f'Ошибка: {e}')
        return ""


def investment_bank(transactions: List[Dict], date: str, limit: int) -> float:
    """Считает сумму, которую можно было отложить в инвесткопилку."""
    try:
        sum_investment_bank = 0.0
        user_date = datetime.strptime(date, '%Y.%m')
        for transaction in transactions:
            transaction_date = datetime.strptime(transaction["Дата операции"], '%d.%m.%Y %H:%M:%S')
            if transaction_date.year == user_date.year and transaction_date.month == user_date.month:
                amount = transaction["Сумма операции"]
                if amount < 0 and transaction["Категория"] not in ["Переводы", "Наличные"]:
                    sum_investment_bank += ((abs(amount) + limit + 1) // limit) * limit - abs(amount)
        return sum_investment_bank
    except Exception as e:
        logger.error(f'Ошибка: {e}')
        return 0.0
