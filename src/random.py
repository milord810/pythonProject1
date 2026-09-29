import pandas as pd
from src.data_frames import csv_reader


def process_bank_search(data:list[dict], search:str):
    search_dict = []
    for id in data:
        if search in id.get('description'):
            search_dict.append(id)

    print(search_dict)

# def process_bank_operations(data:list[dict], categories:list)->dict:
#     pass

if __name__ == '__main__':
    print(csv_reader("transactions.csv"))
    # print(process_bank_search(csv_reader("transactions.csv"), 'Перевод'))
