def filter_by_state(list_dicts: list, key: str = "EXECUTED") -> list:
    """Функция, которая принимает список словарей
    и опционально значение для ключа state (по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению."""

    return [i for i in list_dicts if i.get("state") == key.upper()]


def sort_by_date(list_of_dictionary: list, is_reverse: bool = True) -> list:
    """
    Принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание).
    Функция должна возвращать новый список, отсортированный по дате (date)
    """

    sorted_list_of_dictionary = sorted(list_of_dictionary, key=lambda data: data["date"], reverse=is_reverse)

    return sorted_list_of_dictionary
