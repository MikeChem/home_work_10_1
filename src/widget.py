from src.masks import get_mask_account, get_mask_card_number

def mask_account_card(account_card: str) -> str:
    """
    Принимает один аргумент — строку, содержащую тип и номер карты или счета.
    Возвращает строку с замаскированным номером.
    """

    index_space = account_card.rfind(' ')

    card_name = account_card[:index_space]
    card_number = account_card[index_space + 1:]

    if card_name == 'Счет':
        return f'{card_name} {get_mask_account(card_number)}'
    else:
        return f'{card_name} {get_mask_card_number(card_number)}'

print(mask_account_card(input()))