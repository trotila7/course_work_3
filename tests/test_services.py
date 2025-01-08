import pytest
from datetime import datetime
from src.services import analyze_cashback, investment_bank, search_transactions_by_user_choice
from src.utils import get_data_from_xlsx


@pytest.fixture
def sample_transactions():
    return [
        {"Дата операции": "01.03.2020 10:00:00", "Сумма операции": -100, "Категория": "Супермаркеты", "Кэшбэк": 1},
        {"Дата операции": "15.03.2020 15:30:00", "Сумма операции": -50, "Категория": "Кафе", "Кэшбэк": 0.5},
        {"Дата операции": "25.03.2020 18:00:00", "Сумма операции": -20, "Категория": "Транспорт", "Кэшбэк": 0.2}
    ]


def test_analyze_cashback(sample_transactions):
    result = analyze_cashback(sample_transactions, 2020, 3)
    expected_result = {
        "Супермаркеты": 1.0,
        "Кафе": 0.5,
        "Транспорт": 0.2
    }
    assert result == pytest.approx(expected_result, rel=1e-2)


def test_investment_bank(sample_transactions):
    result = investment_bank(sample_transactions, "2020.03", 50)
    expected_result = 100  # Ожидаемая сумма по логике
    assert result == expected_result


def test_search_transactions_by_user_choice(sample_transactions):
    result = search_transactions_by_user_choice(sample_transactions, "Супермаркеты")
    assert len(result) == 1
    assert result[0]["Категория"] == "Супермаркеты"
