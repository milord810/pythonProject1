import pytest
from src.external_api.py import convertation

from unittest.mock import Mock, patch

from dotenv import load_dotenv

load_dotenv()


def test_convertation_rub(data: dict) -> None:
    data = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }
    assert test_convertation_rub(data) == 31957.58


@patch("src.external_api.API_KEY", "api_key")
@patch("src.external_api.requests.get")
def test_convertation_usd(mock_get):
    transaction = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }
    mock_response = Mock()
    mock_response.json.return_value = {result: 643595.90835}
    mock_get.return_value = mock_response
    result = test_convertation_usd(transaction)
    assert result == 643595.90835
    mock_get.assert_called_once_with(
        f"https://api.apilayer.com/currency_data/convert?to=RUB&from={currency}&amount={amount}",
        headers={"apikey": API_KEY},
    )
