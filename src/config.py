import os
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

# Переменные для работы с API
api_key_currency = os.getenv("API_KEY_CURRENCY")
api_key_stocks = os.getenv("API_KEY_STOCKS")

# Другие параметры
input_date_str = "20.03.2020"
transactions_path = '../data/operations.xls'
year = 2020
month = 5
date = "2020.05"
limit = 50
search = "Перевод"
