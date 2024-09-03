# Проект "Виджет банковских операций" 

## Описание: Это виджет, который показывает несколько последних успешных банковских операций клиента. Проект, который на бэкенде будет готовить данные для отображения в новом виджете. 
* Реализована функция, которая принимает на вход номер карты и возвращает ее маску. Номер карты замаскирован и отображается в формате XXXX XX** **** XXXX, где X — это цифра номера. 
* Реализована функция, которая принимает на вход номер счета и возвращает его маску. Номер счета замаскирован и отображается в формате **XXXX, где X — это цифра номера. 
* Реализована функция, которая принимает один аргумент — строку, содержащую тип и номер карты или счета, возвращает строку с замаскированным номером. Для карт и счетов используйте разные типы маскировки 
* Реализована функция, которая принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407" и возвращает строку с датой в формате "ДД.ММ.ГГГГ"("11.03.2024"). 
* Реализована функция, которая принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует указанному значению. 
* Реализована функция, которая принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание). Функция возвращает новый список, отсортированный по дате (date). 

## Тестирование 
* Наш проект покрыт тестами Pytest. Для их запуска выполните команду:
`pytest`
* Для получения статистики тестов выполните команду:
`pytest --cov`

## Установка: 
1. Клонируйте репозиторий: ``` https://github.com/MikeChem/home_work_10_1/pull/1``` 
2. Установите зависимости: ``` poetry install ``` 

## Использование: 
## Документация: 
## Лицензия:
