import logging
import os
from datetime import datetime, timedelta
from typing import Dict, List

import pandas as pd
import requests

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


def get_data_from_xlsx(path: str) -> List[Dict]:
    """Функция для чтения данных из xlsx файла"""
    try:
        df = pd.read_excel(path)
        logger.info('Файл успешно загружен')
        return df.to_dict(orient='records')
    except Exception as e:
        logger.error(f'Ошибка при загрузке данных из файла: {e}')
        return []


def filter_transactions_by_date(transactions: List[Dict], input_date_str: str) -> List[Dict]:
    """Функция фильтрует транзакции по заданной дате"""
    try:
        input_date = datetime.strptime(input_date_str, '%d.%m.%Y')
        end_date = input_date + timedelta(days=1)
        start_date = datetime(end_date.year, end_date.month, 1)

        def parse_date(date_str: str) -> datetime:
            """Функция для преобразования строки в дату"""
            return datetime.strptime(date_str, '%d.%m.%Y %H:%M:%S')

        filtered_transactions = [transaction for transaction in transactions
                                 if start_date <= parse_date(transaction["Дата операции"]) <= end_date]
        logger.info(f'Фильтрация транзакций с {start_date} до {end_date}')
        return filtered_transactions
    except Exception as e:
        logger.error(f'Ошибка при фильтрации транзакций: {e}')
        return []


def get_cards_data(transactions: List[Dict]) -> List[Dict]:
    """Функция создает словарь с номерами карт и в значения добавляет сумму трат и сумму кэшбека"""
    card_data = {}
    for transaction in transactions:
        card_number = transaction.get('Номер карты')
        if not card_number or str(card_number).strip().lower() == 'nan':
            continue
        amount = float(transaction['Сумма операции'])
        if card_number not in card_data:
            card_data[card_number] = {'total_spent': 0.0, 'cashback': 0.0}
        if amount < 0:
            card_data[card_number]['total_spent'] += abs(amount)
            cashback_value = transaction.get("Кэшбэк")
            if transaction["Категория"] != "Переводы" and transaction["Категория"] != "Наличные":
                if cashback_value is not None:
                    cashback_amount = float(cashback_value)
                    if cashback_amount >= 0:
                        card_data[card_number]['cashback'] += cashback_amount
                    else:
                        card_data[card_number]['cashback'] += amount * -0.01
                else:
                    card_data[card_number]['cashback'] += amount * -0.01
    cards_data = []
    for last_digits, data in card_data.items():
        cards_data.append({
            "last_digits": last_digits,
            "total_spent": round(data['total_spent'], 2),
            "cashback": round(data['cashback'], 2)})
    return cards_data


def get_top_5_transactions(transactions: List[Dict]) -> List[Dict]:
    """Функция принимает список транзакций и выводит топ 5 операций по сумме платежа"""
    sorted_transactions = sorted(transactions, key=lambda x: abs(float(x["Сумма операции"])), reverse=True)
    top_5_sorted_transactions = []
    for transaction in sorted_transactions[:5]:
        date = datetime.strptime(transaction["Дата операции"], '%d.%m.%Y %H:%M:%S').strftime('%d.%m.%Y')
        top_5_sorted_transactions.append({
            "date": date,
            "amount": transaction["Сумма операции"],
            "category": transaction["Категория"],
            "description": transaction["Описание"]
        })
    logger.info('Выделено топ 5 больших транзакций')
    return top_5_sorted_transactions


def get_exchange_rates(currencies: List[str], api_key_currency: str) -> List[Dict]:
    """Функция принимает список кодов валют и возвращает список словарей с валютами и их курсами"""
    exchange_rates = []
    for currency in currencies:
        url = f'https://v6.exchangerate-api.com/v6/{api_key_currency}/latest/{currency}'
        response = requests.get(url)
        logger.info('Выполнен запрос на курс валют')
        if response.status_code == 200:
            data = response.json()
            logger.info(f'Получен ответ от API курса валют: {data}')
            ruble_cost = data["conversion_rates"]["RUB"]
            exchange_rates.append({
                "currency": currency,
                "rate": ruble_cost})
        else:
            logger.error(f'Ошибка API запроса курса валют: {response.status_code}, {response.text}')
            exchange_rates.append({
                "currency": currency,
                "rate": None
            })
    logger.info('Курсы валют созданы')
    return exchange_rates


def get_stocks_cost(companies: List[str], api_key_stocks: str) -> List[Dict]:
    """Функция принимает список кодов компаний и возвращает словарь со стоимостью акций каждой переданной компании"""
    stocks_cost = []
    for company in companies:
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={company}&apikey={api_key_stocks}'
        response = requests.get(url)
        logger.info('Выполнен запрос на курс акций')
        if response.status_code == 200:
            data = response.json()
            logger.info(f'Получен ответ от API курса акций: {data}')
            time_series = data.get("Time Series (Daily)")
            if time_series:
                latest_date = max(time_series.keys())
                latest_data = time_series[latest_date]
                stock_cost = latest_data["4. close"]
                stocks_cost.append({
                    "stock": company,
                    "price": float(stock_cost)})
            else:
                logger.error(f'Ошибка получения данных по акции {company}: {data}')
                stocks_cost.append({
                    "stock": company,
                    "price": None})
        else:
            logger.error(f'Ошибка API запроса курса акций: {response.status_code}, {response.text}')
            stocks_cost.append({
                "stock": company,
                "price": None})
    logger.info('Стоимость акций создана')
    return stocks_cost


def greeting() -> str:
    """Функция определяет время суток и возвращает приветствие в зависимости от времени"""
    now = datetime.now()
    current_hour = now.hour
    if 6 <= current_hour < 12:
        return "Доброе утро"
    elif 12 <= current_hour < 18:
        return "Добрый день"
    elif 18 <= current_hour < 23:
        return "Добрый вечер"
    else:
        return "Доброй ночи"
