from unittest.mock import Mock, patch

from src.external_api import convertation


@patch("requests.get")
def test_convertation(mock_get):
    transaction = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }
    mock_get.return_value.json.return_value = {"result": 645996.836138}
    result = convertation(transaction)
    assert result == 645996.836138

    transaction["operationAmount"]["currency"]["code"] = "RUB"
    result = convertation(transaction)
    assert result == 8221.37
