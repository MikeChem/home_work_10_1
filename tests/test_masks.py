import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234123412341234", "1234 12** **** 1234"),
        ("1234 1234 1234 1234", "1234 12** **** 1234"),
        (1234123412341234, "1234 12** **** 1234"),
        ("card 1234123412341234", "Номер кредитной карты должен содержать только цифры"),
        ("", "Номер кредитной карты должен содержать 16 цифр"),
        ("12341234123412345", "Номер кредитной карты должен содержать 16 цифр"),
    ],
)
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("12341234123412341234", "**1234"),
        (12341234123412341234, "**1234"),
        ("account 12341234123412341234", "Номер счета должен содержать только цифры"),
        ("", "Номер счета должен содержать 20 цифр"),
        ("12341234123412345", "Номер счета должен содержать 20 цифр"),
    ],
)
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected
