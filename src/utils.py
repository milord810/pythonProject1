import json
import logging
import os

from dotenv import load_dotenv
from mypy.cache import read_json

load_dotenv(".env")

API_KEY = os.getenv("API_KEY")

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s: utils.py: %(levelname)s: %(message)s", filename="utils.log", filemode="w"
)

logger = logging.getLogger("read_json")
file_handler = logging.FileHandler("utils.log")
file_formatter = logging.Formatter("%(asctime)s: %(modulename)s: %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def reading_json(filename):
    try:
        logger.info("starting app...")
        with open(filename, encoding="UTF-8") as file:
            data = json.load(file)
            if type(data) is list:
                return data
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        logger.error("failed starting app...")
        return []


if __name__ == "__main__":
    print(read_json("../data/operations.json"))
    transaction = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }
