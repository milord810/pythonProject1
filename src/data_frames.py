import csv

import pandas as pd


def csv_reader(way):
    """Функция для считывания CSV"""
    with open(way) as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            return row


def excel_reader(excel_way):
    """Функция для считывания Excel"""
    excel_df = pd.read_excel(excel_way)
    result = excel_df.to_dict(orient="records")
    return result


if __name__ == "__main__":
    csv_reader("transactions.csv")
    excel_reader("transactions_excel.xlsx")
