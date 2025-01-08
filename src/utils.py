import pandas as pd


def read_transactions(file_path):
    """ Чтение данных из Excel-файла. """
    return pd.read_excel(file_path)
