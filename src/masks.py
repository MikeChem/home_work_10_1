from typing import Union
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="../logs/masks.log",
    filemode="w",
)

mask_card_number_logger = logging.getLogger("masks")
mask_account_logger = logging.getLogger("masks")


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """Функция, которая принимает на вход номер кредитной карты и возвращает его замаскированную версию."""
    try:
        mask_card_number_logger.info("Проверка входящего номера карты на соответствие длины и символам")
        card_number = str(card_number).replace(" ", "")
        if card_number == "":
            mask_card_number_logger.warning("Ошибка ввода")
            return "Номер кредитной карты должен содержать 16 цифр"

        elif not card_number.isdigit():
            mask_card_number_logger.warning("Ошибка ввода")
            return "Номер кредитной карты должен содержать только цифры"

        else:
            if len(card_number) != 16:
                mask_card_number_logger.warning("Ошибка ввода")
                return "Номер кредитной карты должен содержать 16 цифр"

        mask_card_number_logger.info("Получение замаскированного номера карты")
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"

    except Exception as ex:
        mask_card_number_logger.error(f"Произошла ошибка: {ex}")


def get_mask_account(account_number: Union[str, int]) -> str:
    """Принимает на вход номер счета и возвращает его маску"""
    try:
        mask_account_logger.info("Проверка входящего номера счета на соответствие длины и символам")
        account_number = str(account_number)

        if account_number == "":
            mask_account_logger.warning("Ошибка ввода")
            return "Номер счета должен содержать 20 цифр"

        elif not account_number.isdigit():
            mask_account_logger.warning("Ошибка ввода")
            return "Номер счета должен содержать только цифры"

        else:
            if len(account_number) != 20:
                mask_account_logger.warning("Ошибка ввода")
                return "Номер счета должен содержать 20 цифр"

        mask_account_logger.info("Получение замаскированного номера счета")
        return f"**{account_number[-4:]}"

    except Exception as ex:
        mask_account_logger.error(f"Произошла ошибка: {ex}")
