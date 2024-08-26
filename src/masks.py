def get_mask_card_number(card_number: str) -> str:
    """Функция, которая принимает на вход номер кредитной карты и возвращает его замаскированную версию."""

    # Проверяем, что номер карты содержит 16 цифр
    if len(card_number) != 16:
        return "Номер кредитной карты должен содержать 16 цифр"

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Принимает на вход номер счета и возвращает его маску"""

    return f"**{account_number[-4:]}"
