import json
import requests
import os
from dotenv import load_dotenv

load_dotenv(".env")

API_KEY = os.getenv("API_KEY")


def read_json(filename):
    try:
        with open(filename, encoding="UTF-8") as file:
            data = json.load(file)
            if type(data) is list:
                return data
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def convertation(data: dict) -> float:
    """Функция, конвертирующая валюты из USD в RUR"""

    if data["operationAmount"]["currency"]["code"] == "RUB":  # Проверка, если валюта- RUB, возвращает значение
        return float(data["operationAmount"]["amount"])
    if data["operationAmount"]["currency"]["code"] == "USD":  # Проверка, если валюта- USD, возвращает значение в рублях
        response = requests.get(f"https://api.apilayer.com/currency_data/convert?to={RUB}&from={USD}&amount={amount}")
        return float(data["operationAmount"]["amount"] * {response})
    if data["operationAmount"]["currency"]["code"] == "EUR":  # Проверка, если валюта- EUR, возвращает значение в рублях
        response = requests.get(f"https://api.apilayer.com/currency_data/convert?to={RUR}&from={EUR}&amount={amount}")
        return float(data["operationAmount"]["amount"] * {response})

    payload = {
        "to": "RUB",
        "from": data["operationAmount"]["currency"]["code"],
        "amount": data["operationAmount"]["amount"]
    }
    headers = {"apikey": {API_KEY}}


    url = "https://api.apilayer.com/currency_data/convert?to={RUR}&from={EUR}&amount={amount}"

    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    converted_data = response.text

    return float(converted_data)


if __name__ == "__main__":
    # print(read_json("../data/operations.json"))
    transaction = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }

# print(convertation(transaction))
