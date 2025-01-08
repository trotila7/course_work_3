import json
import pytest
import pandas as pd
from src.reports import spending_by_category, spending_by_weekday, spending_by_workday


@pytest.fixture
def mock_data():
    return pd.DataFrame({
        "Дата операции": ["01.05.2020 10:00:00", "15.05.2020 10:00:00", "20.05.2020 10:00:00"],
        "Категория": ["Супермаркеты", "Кафе", "Супермаркеты"],
        "Сумма операции": [-200, -150, -300]
    })


def test_spending_by_category(mock_data):
    result = spending_by_category(mock_data, "Супермаркеты", "2020.05.20")
    assert isinstance(result, str), "Результат должен быть строкой"
    result_dict = json.loads(result)
    assert isinstance(result_dict, list), "Должен быть список транзакций"
    assert len(result_dict) == 2, "Должны быть две транзакции по категории 'Супермаркеты'"


def test_spending_by_weekday(mock_data):
    result = spending_by_weekday(mock_data, "2020.05.20")
    assert isinstance(result, str), "Результат должен быть строкой"
    result_dict = json.loads(result)
    assert isinstance(result_dict, dict), "Результат должен быть словарем"
    assert "Понедельник" in result_dict, "День недели 'Понедельник' должен быть в результате"


def test_spending_by_workday(mock_data):
    result = spending_by_workday(mock_data, "2020.05.20")
    assert isinstance(result, str), "Результат должен быть строкой"
    result_dict = json.loads(result)
    assert isinstance(result_dict, dict), "Результат должен быть словарем"
    assert "Рабочий" in result_dict, "Тип дня 'Рабочий' должен быть в результате"
