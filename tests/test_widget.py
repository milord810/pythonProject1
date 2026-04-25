import pytest

from src.widget import get_date, mask_account_card

@pytest.mark.parametrize(
    "data, masked_data",
    [
        ("Visa Platinum 1596837868705199", "Visa Platinum 1596 83** **** 5199"),
        ("МИР 1234567890001235", "Неверный формат данных"),
        ("Счет 12341234123412341234", "Счет **1234"),
        ("привет", "Неверный формат данных"),
        ("Счет 12341234А2341234", "Неверный формат данных"),
        ("", "Неверный формат данных"),
    ],
)
def test_mask_account_card(data, masked_data):
    """Функция тестирования маскировки номера карты или счёта"""
    assert mask_account_card(data) == masked_data


def test_get_date():
    """ "Функция тестирования введенной даты"""
    assert get_date("2026-03-08T02:26:18.671407") == "08.03.2026"