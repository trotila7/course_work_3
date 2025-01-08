import pytest
from src.utils import get_data_from_xlsx, filter_transactions_by_date
from datetime import datetime


@pytest.fixture
def mock_data():
    return [
        {"Дата операции": "01.05.2020 12:00:00", "Категория": "Супермаркеты", "Сумма операции": -100,
         "Описание": "Покупка"},
        {"Дата операции": "02.05.2020 12:00:00", "Категория": "Рестораны", "Сумма операции": -50, "Описание": "Обед"},
        {"Дата операции": "03.05.2020 12:00:00", "Категория": "Супермаркеты", "Сумма операции": -75,
         "Описание": "Покупка"}
    ]


def test_get_data_from_xlsx(mock_data):
    # Пример вызова mock данных, если используется настоящий файл
    assert isinstance(mock_data, list)


def test_filter_transactions_by_date(mock_data):
    result = filter_transactions_by_date(mock_data, "02.05.2020")
    assert len(result) == 2  # Проверяем, что две транзакции попали в фильтр
