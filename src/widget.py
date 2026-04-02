import masks


def mask_account_card(number_of_count: str) -> str:
    """Функция, которая маскирует принятый номер карты/счета"""
    if "Visa Platinum " in number_of_count:
        return "Visa Platinum " + masks.get_mask_card_number(number_of_count[15:])
    elif "Maestro " in number_of_count:
        return "Maestro " + masks.get_mask_card_number(number_of_count[9:])
    elif "MasterCard " in number_of_count:
        return "MasterCard " + masks.get_mask_card_number(number_of_count[12:])
    elif "Visa Classic " in number_of_count:
        return "Visa Classic " + masks.get_mask_card_number(number_of_count[13:])
    elif "Счет " in number_of_count:
        return "Счет " + masks.get_mask_account(number_of_count[5:])
    else:
        return "Неверный формат данных"

mask_account_card("MasterCard 7158300734726758")

def get_date(input_date: str) -> str:
    """Функция принимает на вход строку и выдает дату в требуемом формате"""
    return input_date[8:10] + '.' + input_date[5:7] + '.' + input_date[0:4]

get_date("2024-03-11T02:26:18.671407")
