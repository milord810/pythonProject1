import csv

import pandas as pd


def csv_reader(way):
    """Функция для считывания CSV"""
    with open(way) as file:
        reader = csv.DictReader(file, delimiter=",")
        next(reader)
        for row in reader:
            return row


def excel_reader(excel_way):
    """Функция для считывания Excel"""
    excel_data = pd.read_excel(excel_way)
    print(excel_data.head())


if __name__ == "__main__":
    csv_reader("transactions.csv")

    excel_reader("transactions_excel.xlsx")
