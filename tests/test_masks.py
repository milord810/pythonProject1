import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "data_cards, masked_data_card",
    [
        ("3215697832156978", "3215 69** **** 6978"),
        ("1234567890123456", "1234 56** **** 3456"),
    ],
)
def test_get_mask_card_number(data_cards, masked_data_card):
    """Тест маскировки номера карты"""
    assert get_mask_card_number(data_cards) == masked_data_card


@pytest.mark.parametrize(
    "data_account, masked_data_account",
    [
        ("32156978321569784444", "**4444"),
        ("12345678901234567890", "**7890"),
    ],
)
def test_get_mask_account(data_account, masked_data_account):
    """Тест маскировки номера счета"""
    assert get_mask_account(data_account) == masked_data_account
