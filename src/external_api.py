import requests
import os
from dotenv import load_dotenv

load_dotenv()

# API_KEY = os.getenv("API_KEY")
API_KEY="PTYyVLoFiWALhiALPA5JaxkefFEz35cU"


def convertation(data: dict) -> float:
    """Функция, конвертирующая валюты из USD в RUB"""

    amount = data.get("operationAmount").get("amount")
    currency = data.get("operationAmount").get("currency").get("code")
    headers = {"apikey": API_KEY}

    if currency == "RUB":  # Проверка, если валюта - RUB, возвращает значение
        return amount

    url = f"https://api.apilayer.com/currency_data/convert?to=RUB&from={currency}&amount={amount}"

    response = requests.request("GET", url, headers=headers).json()

    return response
    print(response)

if __name__ == "__main__":
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

print(convertation(transaction))