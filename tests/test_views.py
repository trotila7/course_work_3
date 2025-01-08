import pytest
from src.views import main
from unittest.mock import patch


@pytest.fixture
def user_settings():
    return {
        "user_currencies": ["USD", "EUR"],
        "user_stocks": ["AAPL", "AMZN"]
    }


@patch("src.views.get_data_from_xlsx")
@patch("src.views.filter_transactions_by_date")
@patch("src.views.get_cards_data")
@patch("src.views.get_exchange_rates")
@patch("src.views.get_stocks_cost")
@patch("src.views.get_top_5_transactions")
def test_main(mock_get_top_5_transactions, mock_get_stocks_cost, mock_get_exchange_rates,
              mock_get_cards_data, mock_filter_transactions_by_date, mock_get_data_from_xlsx, user_settings):
    mock_get_data_from_xlsx.return_value = [{"Дата операции": "01.03.2020 10:00:00", "Сумма операции": -100}]
    mock_filter_transactions_by_date.return_value = [{"Дата операции": "01.03.2020 10:00:00", "Сумма операции": -100}]
    mock_get_cards_data.return_value = [{"last_digits": "1234", "total_spent": 100, "cashback": 1}]
    mock_get_exchange_rates.return_value = [{"currency": "USD", "rate": 73.5}]
    mock_get_stocks_cost.return_value = [{"stock": "AAPL", "price": 150}]
    mock_get_top_5_transactions.return_value = [
        {"date": "01.03.2020", "amount": -100, "category": "Супермаркеты", "description": "Покупка"}]

    result = main("2020.03.20", user_settings, "api_key_currency", "api_key_stocks")
    assert "greeting" in result
    assert "cards" in result
    assert "top_transactions" in result
    assert "exchange_rates" in result
    assert "stocks" in result
