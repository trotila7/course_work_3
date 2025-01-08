import pytest
from datetime import datetime
from src.utils import get_data_from_xlsx, filter_transactions_by_date


def test_get_data_from_xlsx():
    # Предположим, что файл данных существует
    result = get_data_from_xlsx('../data/operations.xls')
    assert isinstance(result, list), "Данные должны быть в виде списка словарей"
    assert len(result) > 0, "Список данных не должен быть пустым"


def test_filter_transactions_by_date():
    transactions = [
        {"Дата операции": "01.05.2020 10:00:00", "Категория": "Супермаркеты", "Сумма операции": -200},
        {"Дата операции": "15.05.2020 10:00:00", "Категория": "Кафе", "Сумма операции": -150},
        {"Дата операции": "20.05.2020 10:00:00", "Категория": "Супермаркеты", "Сумма операции": -300}
    ]
    input_date = "20.05.2020"
    filtered_transactions = filter_transactions_by_date(transactions, input_date)
    assert len(filtered_transactions) == 1, "Фильтрация не вернула нужное количество транзакций"
    assert filtered_transactions[0]["Дата операции"] == datetime.strptime("20.05.2020 10:00:00",
                                                                          "%d.%m.%Y %H:%M:%S"), "Дата фильтрации неверна"


def test_greeting():
    """Проверка корректности возвращаемого приветствия"""
    greeting_message = greeting()
    assert greeting_message in ["Доброе утро", "Добрый день", "Добрый вечер", "Доброй ночи"], "Некорректное приветствие"
