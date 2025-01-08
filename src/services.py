import pandas as pd


def analyze_transactions(data: pd.DataFrame, year: int, month: int):
    """ Анализ транзакций по году и месяцу. """
    filtered_data = data[(data['Дата операции'].dt.year == year) &
                         (data['Дата операции'].dt.month == month)]
    categories_summary = filtered_data.groupby('Категория')['Сумма операции'].sum()
    return categories_summary.to_json()
