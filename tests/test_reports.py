import pytest
from src.reports import spending_by_category, spending_by_weekday, spending_by_workday
import pandas as pd


@pytest.fixture
def sample_transactions():
    return [
        {"Дата операции": "01.03.2020 10:00:00", "Сумма операции": -100, "Категория": "Супермаркеты"},
        {"Дата операции": "15.03.2020 15:30:00", "Сумма операции": -50, "Категория": "Кафе"},
        {"Дата операции": "25.03.2020 18:00:00", "Сумма операции": -20, "Категория": "Транспорт"}
    ]


def test_spending_by_category(sample_transactions):
    df = pd.DataFrame(sample_transactions)
    result = spending_by_category(df, "Супермаркеты", "2020.03.20")
    assert '"Категория": "Супермаркеты"' in result


def test_spending_by_weekday(sample_transactions):
    df = pd.DataFrame(sample_transactions)
    result = spending_by_weekday(df, "2020.03.20")
    assert '"Понедельник":' in result


def test_spending_by_workday(sample_transactions):
    df = pd.DataFrame(sample_transactions)
    result = spending_by_workday(df, "2020.03.20")
    assert '"Рабочий":' in result
