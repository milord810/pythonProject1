from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(text: str) -> str:
    """Функция, которая маскирует принятый номер карты/счета"""
    if not text:
        return "Данные не введены"
    splited_text = text.split()
    card_or_account_info = " ".join(splited_text[:-1])
    number = splited_text[-1]

    if number.isdigit() and len(number) == 20:
        return f"{card_or_account_info} {get_mask_account(number)}"
    elif number.isdigit() and len(number) == 16:
        return f"{card_or_account_info} {get_mask_card_number(number)}"
    else:
        return "Неверный формат данных"


def get_date(input_date: str) -> str:
    """Функция принимает на вход строку и выдает дату в требуемом формате"""
    return str(input_date[8:10] + "." + input_date[5:7] + "." + input_date[0:4])
