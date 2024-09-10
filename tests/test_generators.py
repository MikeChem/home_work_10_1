import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(dict_test_transaction):

    generator = filter_by_currency(dict_test_transaction)

    assert next(generator) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }

    assert next(generator) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }

    assert next(generator) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-05-05T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }

    generator = filter_by_currency(dict_test_transaction, "EURO")

    assert next(generator) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "EURO", "code": "EURO"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }

    generator = filter_by_currency(dict_test_transaction, "RUB")

    with pytest.raises(StopIteration):
        next(generator)


def test_transaction_descriptions(dict_test_transaction):

    generator = transaction_descriptions(dict_test_transaction)

    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"

    with pytest.raises(StopIteration):
        next(generator)


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (10, 12, ["0000 0000 0000 0010", "0000 0000 0000 0011", "0000 0000 0000 0012"]),
        (100, 102, ["0000 0000 0000 0100", "0000 0000 0000 0101", "0000 0000 0000 0102"]),
        (0, 1, []),
        (9999999999999999, 9999999999999999, ["9999 9999 9999 9999"]),
        (9999999999999999, 10000000000000000, []),
    ],
)
def test_card_number_generator(start, stop, expected):

    generator = card_number_generator(start, stop)

    results = list(generator)

    assert results == expected


# def test_card_number_generator(card_number, expected):
#
#     result = card_number_generator(1, 2)
#
#     assert next(result) == expected
