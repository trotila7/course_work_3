import pytest
from src.utils import get_data_from_xlsx, filter_transactions_by_date
from datetime import datetime


@pytest.fixture
def sample_transactions():
    return [
        {"Дата операции": "01.03.2020 10:00:00", "Сумма операции": 100, "Категория": "Супермаркеты"},
        {"Дата операции": "15.03.2020 15:30:00", "Сумма операции": -50, "Категория": "Кафе"},
        {"Дата операции": "25.03.2020 18:00:00", "Сумма операции": -20, "Категория": "Транспорт"}
    ]


def test_get_data_from_xlsx(sample_transactions, tmp_path):
    # Создание временного файла
    file = tmp_path / "test_operations.xls"
    df = pd.DataFrame(sample_transactions)
    df.to_excel(file, index=False)

    result = get_data_from_xlsx(str(file))
    assert len(result) == 3
    assert result[0]["Дата операции"] == "01.03.2020 10:00:00"


def test_filter_transactions_by_date(sample_transactions):
    filtered_transactions = filter_transactions_by_date(sample_transactions, "15.03.2020")
    assert len(filtered_transactions) == 2
    assert filtered_transactions[0]["Дата операции"] == "01.03.2020 10:00:00"
