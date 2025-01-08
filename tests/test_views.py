import json
import pytest
from src.views import main


def test_main():
    input_date = "20.03.2020"
    user_settings = {
        "user_currencies": ["USD", "EUR"],
        "user_stocks": ["AAPL", "AMZN", "GOOGL"]
    }
    api_key_currency = "mock_api_key_currency"
    api_key_stocks = "mock_api_key_stocks"

    response = main(input_date, user_settings, api_key_currency, api_key_stocks)
    data = json.loads(response)

    # Проверка, что ключи присутствуют в ответе
    assert "greeting" in data
    assert "cards" in data
    assert "top_transactions" in data
    assert "exchange_rates" in data
    assert "stocks" in data

    # Проверка, что валюты и акции отображаются корректно
    assert isinstance(data["exchange_rates"], list)
    assert isinstance(data["stocks"], list)
    assert isinstance(data["cards"], list)
    assert isinstance(data["top_transactions"], list)
