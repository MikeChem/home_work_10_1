from typing import Union


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """Функция, которая принимает на вход номер кредитной карты и возвращает его замаскированную версию."""

    card_number = str(card_number).replace(" ", "")

    if card_number == "":
        return "Номер кредитной карты должен содержать 16 цифр"

    elif not card_number.isdigit():
        return "Номер кредитной карты должен содержать только цифры"

    else:
        if len(card_number) != 16:
            return "Номер кредитной карты должен содержать 16 цифр"

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: Union[str, int]) -> str:
    """Принимает на вход номер счета и возвращает его маску"""

    account_number = str(account_number)

    if account_number == "":
        return "Номер счета должен содержать 20 цифр"

    elif not account_number.isdigit():
        return "Номер счета должен содержать только цифры"

    else:
        if len(account_number) != 20:
            return "Номер счета должен содержать 20 цифр"

    return f"**{account_number[-4:]}"
