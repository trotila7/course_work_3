import json
import pytest
from src.services import analyze_cashback, investment_bank, search_transactions_by_user_choice


@pytest.fixture
def mock_transactions():
    return [
        {"Дата операции": "01.05.2020 10:00:00", "Категория": "Супермаркеты", "Сумма операции": -200, "Кэшбэк": 10},
        {"Дата операции": "15.05.2020 10:00:00", "Категория": "Кафе", "Сумма операции": -150, "Кэшбэк": 5},
        {"Дата операции": "20.05.2020 10:00:00", "Категория": "Супермаркеты", "Сумма операции": -300, "Кэшбэк": 15}
    ]


def test_analyze_cashback(mock_transactions):
    result = analyze_cashback(mock_transactions, 2020, 5)
    result_dict = json.loads(result)
    assert isinstance(result_dict, dict), "Результат должен быть словарем"
    assert "Супермаркеты" in result_dict, "Кэшбэк по категории 'Супермаркеты' не найден"
    assert result_dict["Супермаркеты"] == 25, "Неверная сумма кэшбэка"


def test_investment_bank(mock_transactions):
    result = investment_bank(mock_transactions, "2020.05", 50)
    assert isinstance(result, float), "Результат должен быть числом"
    assert result > 0, "Инвесткопилка должна вернуть положительную сумму"


def test_search_transactions_by_user_choice(mock_transactions):
    result = search_transactions_by_user_choice(mock_transactions, "Супермаркеты")
    result_list = json.loads(result)
    assert isinstance(result_list, list), "Результат должен быть списком"
    assert len(result_list) > 0, "По запросу 'Супермаркеты' должны быть результаты"
