import pandas as pd


def get_data_from_xlsx(path: str) -> list:
    """Чтение транзакций из файла Excel"""
    try:
        df = pd.read_excel(path)
        return df.to_dict(orient='records')
    except Exception as e:
        print(f'Ошибка: {e}')
        return []
