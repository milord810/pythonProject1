import csv

import pandas as pd


def csv_reader(way):
    """Функция для считывания CSV"""
    with open(way) as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            print(row['id'], row['state'], row['amount'], row['currency_name'], row['currency_code'])


def excel_reader(excel_way):
    """Функция для считывания Excel"""
    excel_df = pd.read_excel(excel_way)
    print(excel_df.shape)
    print(excel_df.head())


if __name__ == "__main__":
    csv_reader("transactions.csv")

    excel_reader("transactions_excel.xlsx")
