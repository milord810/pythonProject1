import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


def convertation(data: dict) -> float:
    """Функция, конвертирующая валюты в RUB"""

    amount = data.get("operationAmount").get("amount")
    currency = data.get("operationAmount").get("currency").get("code")
    headers = {"apikey": API_KEY}

    if currency == "RUB":  # Проверка, если валюта - RUB, возвращает значение
        return float(amount)

    url = f"https://api.apilayer.com/currency_data/convert?to=RUB&from={currency}&amount={amount}"

    response:dict = requests.get(url, headers=headers).json()

    return response.get("result")
