import json

from src.data_frames import csv_reader, excel_reader
from src.generators import filter_by_currency
from src.processing import sort_by_date, filter_by_state
from src.regular import process_bank_search


question1 = "Отсортировать операции по дате? Да/Нет"
question2 = "Отсортировать по возрастанию или по убыванию?"
question3 = "Выводить только рублевые транзакции? Да/Нет"
question4 = "Отфильтровать список транзакций по определенному слову в описании? Да/Нет"


# получение данных от пользователя:
def change_type():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")
    ans1 = int(input())  # Выбор типа обрабатываемого файла
    if ans1 == 1:
        with open('data.json', 'r', encoding='utf-8') as file:
            datafile = json.load(file)
        print("Для обработки выбран JSON-файл")

        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")

        ans2 = str(input())  # Запрос параметра для фильтрации
        ans2_up = ans2.upper()  # Убираем чувствительность к регистру
        filter_by_state(datafile, ans2_up)
        """ Функция фильтрует по статусу """
        if ans2 in datafile:
            print(f"Операции отфильтрованы по статусу {ans2_up}")
        else:
            print(f"Статус операции {ans2} недоступен")
        print(question1)  # Программа: Отсортировать операции по дате? Да/Нет
        ans3 = str(input())  # Запрос ответа по сортировке
        ans3_up = ans3.upper()  # Убираем чувствительность к регистру
        if ans3_up == "ДА":
            sort_by_date(datafile)
            """ Функция сортирует по дате """
        elif ans3_up == "НЕТ":
            print("Сортировка по дате не выполняется")
        else:
            print("Невозможный вариант сортировки")
        print(question2)  # Программа: Отсортировать по возрастанию или по убыванию?
        ans4 = str(input())  # Запрос ответа
        ans4_up = ans4.upper()  # Убираем чувствительность к регистру
        if ans4_up == "ПО ВОЗРАСТАНИЮ":
            sorted(datafile, key=None, reverse=False)
            """ Функция сортирует по возрастанию"""
        elif ans4_up == "ПО УБЫВАНИЮ":
            sorted(datafile, key=None, reverse=True)
            """ Функция сортирует по убыванию"""
        else:
            print("Невозможный вариант сортировки")
        print(question3)  # Программа: Выводить только рублевые транзакции? Да/Нет
        ans5 = str(input())  # Запрос ответа
        ans5_up = ans5.upper()  # Убираем чувствительность к регистру
        if ans5_up == "ДА":
            filter_by_currency(datafile, 'RUB')
        elif ans5_up == "НЕТ":
            print("Сортировка по валюте не выполняется")
        else:
            print("Невозможный вариант сортировки")
        print(question4)  # Отфильтровать список транзакций по определенному слову в описании? Да/Нет
        ans6 = str(input())  # Запрос ответа
        ans6_up = ans6.upper()  # Убираем чувствительность к регистру
        if ans6_up == "ДА":
            print("Введите слово для поиска...")
            ans6_1 = str(input())
            process_bank_search(datafile, ans6_1)
        else:
            print("Поиск по слову не выбран")

        if datafile == None:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        else:
            print('Распечатываю итоговый список транзакций...')
            print(datafile)

    elif ans1 == 2:
        datafile = csv_reader("transactions.csv")
        print("Для обработки выбран CSV-файл")

        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")

        ans2 = str(input())  # Запрос параметра для фильтрации
        ans2_up = ans2.upper()  # Убираем чувствительность к регистру
        filter_by_state(datafile, ans2_up)
        """ Функция фильтрует по статусу """
        if ans2 in datafile:
            print(f"Операции отфильтрованы по статусу {ans2_up}")
        else:
            print(f"Статус операции {ans2} недоступен")
        print(question1)  # Программа: Отсортировать операции по дате? Да/Нет
        ans3 = str(input())  # Запрос ответа по сортировке
        ans3_up = ans3.upper()  # Убираем чувствительность к регистру
        if ans3_up == "ДА":
            sort_by_date(datafile)
            """ Функция сортирует по дате """
        elif ans3_up == "НЕТ":
            print("Сортировка по дате не выполняется")
        else:
            print("Невозможный вариант сортировки")
        print(question2)  # Программа: Отсортировать по возрастанию или по убыванию?
        ans4 = str(input())  # Запрос ответа
        ans4_up = ans4.upper()  # Убираем чувствительность к регистру
        if ans4_up == "ПО ВОЗРАСТАНИЮ":
            sorted(datafile, key=None, reverse=False)
            """ Функция сортирует по возрастанию"""
        elif ans4_up == "ПО УБЫВАНИЮ":
            sorted(datafile, key=None, reverse=True)
            """ Функция сортирует по убыванию"""
        else:
            print("Невозможный вариант сортировки")
        print(question3)  # Программа: Выводить только рублевые транзакции? Да/Нет
        ans5 = str(input())  # Запрос ответа
        ans5_up = ans5.upper()  # Убираем чувствительность к регистру
        if ans5_up == "ДА":
            filter_by_currency(datafile, 'RUB')
        elif ans5_up == "НЕТ":
            print("Сортировка по валюте не выполняется")
        else:
            print("Невозможный вариант сортировки")
        print(question4)  # Отфильтровать список транзакций по определенному слову в описании? Да/Нет
        ans6 = str(input())  # Запрос ответа
        ans6_up = ans6.upper()  # Убираем чувствительность к регистру
        if ans6_up == "ДА":
            print("Введите слово для поиска...")
            ans6_1 = str(input())
            process_bank_search(datafile, ans6_1)
        else:
            print("Поиск по слову не выбран")

        if datafile == None:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        else:
            print('Распечатываю итоговый список транзакций...')
            print(datafile)


    elif ans1 == 3:
        datafile = excel_reader("transactions_excel.xlsx")
        print("Для обработки выбран XLSX-файл")

        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")

        ans2 = str(input())  # Запрос параметра для фильтрации
        ans2_up = ans2.upper()  # Убираем чувствительность к регистру
        filter_by_state(datafile, ans2_up)
        """ Функция фильтрует по статусу """
        if ans2 in datafile:
            print(f"Операции отфильтрованы по статусу {ans2_up}")
        else:
            print(f"Статус операции {ans2} недоступен")
        print(question1)  # Программа: Отсортировать операции по дате? Да/Нет
        ans3 = str(input())  # Запрос ответа по сортировке
        ans3_up = ans3.upper()  # Убираем чувствительность к регистру
        if ans3_up == "ДА":
            sort_by_date(datafile)
            """ Функция сортирует по дате """
        elif ans3_up == "НЕТ":
            print("Сортировка по дате не выполняется")
        else:
            print("Невозможный вариант сортировки")
        print(question2)  # Программа: Отсортировать по возрастанию или по убыванию?
        ans4 = str(input())  # Запрос ответа
        ans4_up = ans4.upper()  # Убираем чувствительность к регистру
        if ans4_up == "ПО ВОЗРАСТАНИЮ":
            sorted(datafile, key=None, reverse=False)
            """ Функция сортирует по возрастанию"""
        elif ans4_up == "ПО УБЫВАНИЮ":
            sorted(datafile, key=None, reverse=True)
            """ Функция сортирует по убыванию"""
        else:
            print("Невозможный вариант сортировки")
        print(question3)  # Программа: Выводить только рублевые транзакции? Да/Нет
        ans5 = str(input())  # Запрос ответа
        ans5_up = ans5.upper()  # Убираем чувствительность к регистру
        if ans5_up == "ДА":
            filter_by_currency(datafile, 'RUB')
        elif ans5_up == "НЕТ":
            print("Сортировка по валюте не выполняется")
        else:
            print("Невозможный вариант сортировки")
        print(question4)  # Отфильтровать список транзакций по определенному слову в описании? Да/Нет
        ans6 = str(input())  # Запрос ответа
        ans6_up = ans6.upper()  # Убираем чувствительность к регистру
        if ans6_up == "ДА":
            print("Введите слово для поиска...")
            ans6_1 = str(input())
            process_bank_search(datafile, ans6_1)
        else:
            print("Поиск по слову не выбран")

        if datafile == None:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        else:
            print('Распечатываю итоговый список транзакций...')
            print(datafile)

    else:
        print("Введено некорректное значение")

change_type()
