import os
from dotenv import load_dotenv
from src.utils import get_data_from_xlsx

# Загружаем переменные из .env файла
load_dotenv()

# Настройки API
api_key_currency = os.getenv("API_KEY_CURRENCY")
api_key_stocks = os.getenv("API_KEY_STOCKS")

# Параметры фильтрации транзакций
input_date_str = "20.03.2020"
transactions_path = r'../data/operations.xls'
transactions = get_data_from_xlsx(transactions_path)

# Настройки для расчета
year = 2020
month = 5
date = "2020.05"
limit = 50
search = "Перевод"
