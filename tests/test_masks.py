from src.masks import get_mask_card_number

def test_get_mask_card_number():
    assert get_mask_card_number('1234123412341234') == '1234 12** **** 1234'
    assert get_mask_card_number('12341234123412345') == "Номер кредитной карты должен содержать 16 цифр"
    assert get_mask_card_number(1234123412341234)
