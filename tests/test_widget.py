import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "account_card, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("card 1234123412341234", "card 1234 12** **** 1234"),
        ("", "Неверные данные"),
        ("12341234123412345", "Неверные данные"),
    ],
)
def test_mask_account_card(account_card, expected):
    assert mask_account_card(account_card) == expected


@pytest.mark.parametrize(
    "date_error, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024-03-11", "11.03.2024"),
        ("", "Неверные данные"),
    ],
)
def test_get_date(date_error, expected):
    assert get_date(date_error) == expected
