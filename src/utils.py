import json
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


if __name__ == "__main__":
    print(read_json("../data/operations.json"))
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
