import pandas as pd


def generate_report(data: pd.DataFrame, output_file: str):
    """ Генерация отчета в Excel. """
    data.to_excel(output_file, index=False)
