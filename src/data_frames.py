import csv

import pandas as pd


def csv_reader(way):
    """Функция для считывания CSV"""
    df = pd.read_csv(way, encoding="UTF-8", delimiter=";")
    result_csv = df.to_dict(orient="records")
    return result_csv


def excel_reader(excel_way, encoding="UTF-8"):
    """Функция для считывания Excel"""
    excel_df = pd.read_excel(excel_way)
    result = excel_df.to_dict(orient="records")
    return result


if __name__ == "__main__":
    csv_reader("transactions.csv")
    excel_reader("transactions_excel.xlsx")
