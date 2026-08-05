import logging

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s: masks.py: %(levelname)s: %(message)s", filename="masks.log", filemode="w"
)

masks_logger = logging.getLogger("get_mask_card_number")
file_handler = logging.FileHandler("masks.log")
file_formatter = logging.Formatter("%(asctime)s: %(module)s: %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
masks_logger.addHandler(file_handler)
masks_logger.setLevel(logging.DEBUG)


def get_mask_card_number(text: str) -> str:
    """Функция, маскирующая номер карты"""
    masks_logger.info("starting mask_card_number...")
    if len(text) != 16:
        masks_logger.error("invalid value...")
        return "Недопустимое значение"
    masks_logger.info("return mask card number...")
    return str(text[0:4] + " " + text[4:6] + "**" + " " + "****" + " " + text[-4:])


get_mask_card_number("7000792289606361")


def get_mask_account(text: str) -> str:
    """Функция, возвращающая ** и последние 4 цифры"""
    masks_logger.info("starting get mask account...")
    if len(text) != 20:
        masks_logger.error("invalid value...")
        return "Недопустимое значение"
    masks_logger.info("return mask account...")
    return str("**" + text[-4:])


get_mask_account("73654108430135874305")
