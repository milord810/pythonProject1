import re
import pandas as pd
import re
from collections import Counter
from src.data_frames import csv_reader


def process_bank_search(data:list[dict], search:str) -> list[dict]:
    """ Функция принимает список словарей и строку поиска, возвращает список словарей содержащих строку из поиска"""
    search_dict = []
    pattern = re.compile(search, re.IGNORECASE)
    for i in data:
        if pattern.search(str(i.get('description', ''))):
            search_dict.append(i)

    return search_dict


def process_bank_operations(data:list[dict], categories:list)->dict:
    """ Функция принимает список словарей с данными о банковских операциях и список категорий операций и возвращает словарь с ключами и значениями"""
    operations_dict = []
    for i in data:
        if i['description'] in categories:
            operations_dict.append(i['description'])

    return dict(Counter(operations_dict))


if __name__ == '__main__':
    # print(csv_reader("transactions.csv"))
    a = csv_reader("transactions.csv")
    print(*(process_bank_search(a, 'открытие')), sep='\n')
    print(process_bank_operations(a, ["Перевод организации", "Перевод с карты на карту", "Открытие вклада"]))