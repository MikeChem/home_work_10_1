from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """
    Принимает один аргумент — строку, содержащую тип и номер карты или счета.
    Возвращает строку с замаскированным номером.
    """

    index_space = account_card.rfind(" ")

    card_name = account_card[:index_space]
    card_number = account_card[index_space + 1 :]

    if len(card_number) == 20:
        return f"{card_name} {get_mask_account(card_number)}"
    elif len(card_number) == 16:
        return f"{card_name} {get_mask_card_number(card_number)}"

    else:
        return "Неверные данные"


def get_date(date_error: str) -> str:
    """
    Принимает на вход строку с датой в формате
    '2024-03-11T02:26:18.671407'
    и возвращает строку с датой в формате
    'ДД.ММ.ГГГГ'
    """

    date_fix = date_error[:10]

    if len(date_error) < 10:
        return "Неверные данные"

    return ".".join(date_fix.split("-")[::-1])
