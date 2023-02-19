"""
Задание №7
Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
- Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна
- Для простоты договоримся, что год может быть в диапазоне [1, 9999]
- Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь
- Проверку года на високосность вынести в отдельную защищённую функцию
"""

MIN_YEAR = 1
MAX_YEAR = 9999
FOUR = 4
HUNDRED = 100
FOUR_HUNDRED = 400
ZERO = 0
DAYS_28 = range(1, 28 + 1)
DAYS_29 = range(1, 29 + 1)
DAYS_30 = range(1, 30 + 1)
DAYS_31 = range(1, 31 + 1)


def get_date(date: list[str]) -> bool:
    day = int(date[0])
    month = int(date[1])
    year = int(date[2])
    res = True if MIN_YEAR <= year <= MAX_YEAR and (month == 1 and day in DAYS_31) \
        or (month == 2 and (day in DAYS_28 or day in DAYS_29)) or (month == 3 and day in DAYS_31) \
        or (month == 4 and day in DAYS_30) or (month == 5 and day in DAYS_31) \
        or (month == 6 and day in DAYS_30) or (month == 7 and day in DAYS_31) \
        or (month == 8 and day in DAYS_31) or (month == 9 and day in DAYS_30) \
        or (month == 10 and day in DAYS_31) or (month == 11 and day in DAYS_30) \
        or (month == 10 and day in DAYS_31) else False
    if res:
        print(_leap_year(year))
    return res


def _leap_year(year: int) -> str:
    return 'Год обычный' if year % FOUR != ZERO or year % HUNDRED == ZERO and year % FOUR_HUNDRED != ZERO \
        else 'Год високосный'


if __name__ == '__main__':
    print(get_date(input('Введите дату в формате DD.MM.YYYY: ').split('.')))
