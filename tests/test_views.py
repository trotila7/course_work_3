import pytest
from src.views import main
from unittest.mock import patch
import json
import os


# Мокируем настройки пользователя
@pytest.fixture
def mock_user_settings():
    mock_settings = {
        "user_currencies": ["USD", "EUR"],
        "user_stocks": ["AAPL", "GOOGL"]
    }
    with open('./user_settings.json', 'r') as f:
        json.dump(mock_settings, f)
    yield 'user_settings.json'
    os.remove('user_settings.json')


def test_main(mock_user_settings):
    with open(mock_user_settings, 'r') as file:
        user_settings = json.load(file)

    result = main("2020.05.03", user_settings, "fake_api_key", "fake_api_key")
    assert isinstance(result, str)  # Ожидаем, что результат будет строкой
