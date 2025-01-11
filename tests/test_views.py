import json
from unittest.mock import mock_open, patch

import pytest

from src.views import main


# Мокируем настройки пользователя
@pytest.fixture
def mock_user_settings():
    mock_settings = {
        "user_currencies": ["USD", "EUR"],
        "user_stocks": ["AAPL", "GOOGL"]
    }

    # Используем mock_open для имитации работы с файлом
    mock_file = mock_open(read_data=json.dumps(mock_settings))

    with patch("builtins.open", mock_file):
        yield 'user_settings.json'

    # Здесь не нужно удалять файл, так как используем mock_open
    # mock_file() автоматически удалит "файл" после завершения теста


def test_main(mock_user_settings):
    with open(mock_user_settings, 'r') as file:
        user_settings = json.load(file)

    result = main("2020.05.03", user_settings, "fake_api_key", "fake_api_key")
    assert isinstance(result, str)  # Ожидаем, что результат будет строкой
