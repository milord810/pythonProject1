def get_mask_card_number(text: str) -> str:
    """Функция, маскирующая номер карты"""
    return str(text[0:4] + " " + text[4:6] + "**" + " " + "****" + " " + text[-4:])


get_mask_card_number("7000792289606361")


def get_mask_account(text: str) -> str:
    """Функция, возвращающая ** и последние 4 цифры"""
    return str("**" + text[-4:])


get_mask_account("73654108430135874305")
