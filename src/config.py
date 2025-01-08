import os
from dotenv import load_dotenv

load_dotenv()

api_key_currency = os.getenv("API_KEY_CURRENCY")
api_key_stocks = os.getenv("API_KEY_STOCKS")
input_date_str = "20.03.2020"  # дата для анализа
transactions_path = '../data/operations.xls'
