"""
Задание №7
Функция получает на вход словарь с названием компании в качестве ключа
и списком с доходами и расходами (3-10 чисел) в качестве значения
- Вычислите итоговую прибыль или убыток каждой компании
- Если все компании прибыльные, верните истину, а если хотя бы одна убыточная - ложь
"""
ZERO = 0


def accounting(companies: dict[str, list[int]]) -> dict[str, int]:
    companies_dict = {}
    for key, value in companies.items():
        companies_dict[key] = sum(value)
    profit = all(map(lambda x: x > ZERO, companies_dict.values()))
    print(profit)
    return companies_dict


res = accounting({'Mebel': [100_000, 79_500, 105_000, -90_000],
                  'Fyord': [900_000, -790_000, 1_500_000, -850_000],
                  'PIK': [10_000_000, -7_900_500, 10_050_000, -190_000],
                  'Macrosoft': [-10_000_000, -790_000, 10_500_000, -8_000_000]})
print(res)

"""
Задание №8
Создайте несколько переменных заканчивающихся и не оканчивающихся на “s”
- Напишите функцию, которая при запуске заменяет содержимое переменных 
оканчивающихся на s (кроме переменной из одной буквы s) на None
- Значения не удаляются, а помещаются в одноимённые переменные без s на конце
"""

cars = 'Автомобили'
base = 'База'
cartoons = 'Мультики'
s = 'Переменная'
pie = 'Пирог'
cats = 'Коты'
ONE = 1


def change_func(*args):
    my_dict = {}
    for key, value in globals().items():
        if len(key) != ONE and key.endswith('s'):
            my_dict.setdefault(key[:-1], globals()[key])
            globals()[key] = None
    return my_dict


res = change_func(cars, base, cartoons, pie, cats)
print(res)

"""2. Напишите функцию для транспонирования матрицы"""

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]


def trans_matrix(matrix: list[list[int]]) -> list[list[int]]:
    trans_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            trans_matrix[i][j] = matrix[j][i]
    return trans_matrix


res = trans_matrix(matrix)
print(res)

"""
3. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
где ключ - значение переданного аргумента, а значение - имя аргумента. 
Если ключ не хешируем, используйте его строковое представление
"""


def reverse_dict(some_dict):
    res_dict = {}
    for key, value in some_dict.items():
        if isinstance(value, list | dict | set):
            res_dict.setdefault(str(value), key)
        else:
            res_dict.setdefault(value, key)

    return res_dict


some_dict = {'name': 'Vasya', 'age': 25, 'hobby': 'fitnes', 13: True, False: ['NAN', 0, 'null']}
res = reverse_dict(some_dict)
print(res)

"""
4. Возьмите задачу о банкомате из семинара 2. 
Разбейте её на отдельные операции - функции. 
Дополнительно сохраняйте все операции поступления и снятия средств в список
"""

from decimal import Decimal, getcontext

ZERO = 0
DIVISIBLE = 50
SERIAL_COUNT = 3
THREE_PERCENT = 1.03
EXTRACT_PERCENT = 0.015
MIN_FEE = 30
MAX_FEE = 600
RICHNESS = 5_000_000
RICHNESS_FEE = 0.1

balance = ZERO
counter = ZERO
log = []
getcontext().prec = 10


def action():
    global balance
    global counter

    while True:
        action = int(input('Введите требуемое действие:\n'
                           '1 - Пополнить счёт\n'
                           '2 - Снять наличные\n'
                           '3 - Выйти\n'
                           '-> '))
        if action == 1:
            return cash_deposit()
        elif action == 2:
            return cash_extract()
        elif action == 3:
            return cash_machine_exit()
        else:
            print('Нет такого действия. Попытайтесь ещё', 50 * '-', sep='\n')


def cash_deposit():
    global balance
    global counter
    cash_deposit = int(input('Внесите наличные кратные 50 у.е.: '))
    if Decimal(balance) >= RICHNESS:
        balance -= Decimal(balance) * Decimal(RICHNESS_FEE)
    if cash_deposit > ZERO == cash_deposit % DIVISIBLE:
        counter += 1
        balance += Decimal(cash_deposit)
        if counter == SERIAL_COUNT:
            balance *= Decimal(THREE_PERCENT)
            counter = ZERO
        print(f'На вашем счёте: {Decimal(balance)} у.е.\n{50 * "-"}')
        log.append(f'Внесено на депозит +{cash_deposit} у.е. Баланс: {balance} у.е.')
        return action()
    else:
        print(f'Ввели неверную сумму. На вашем счёте: {Decimal(balance)} у.е.\n{50 * "-"}')
        return action()


def cash_extract():
    global balance
    global counter
    cash_extract = int(input('Введите сумму для снятия кратные 50 у.е.: '))
    if Decimal(balance) >= RICHNESS:
        balance -= Decimal(balance) * Decimal(RICHNESS_FEE)
    if cash_extract > ZERO == cash_extract % DIVISIBLE:
        counter += 1
        cash_extract_percent = cash_extract * EXTRACT_PERCENT
        if cash_extract_percent < MIN_FEE:
            balance -= Decimal(cash_extract - MIN_FEE)
        elif cash_extract_percent > MAX_FEE:
            balance -= Decimal(cash_extract - MAX_FEE)
        else:
            balance -= Decimal(cash_extract - cash_extract_percent)
        if balance < ZERO:
            print('Недостаточно средств на счёте!')
            action()
        if counter == SERIAL_COUNT:
            balance *= THREE_PERCENT
            counter = ZERO
        print(f'На вашем счёте: {Decimal(balance)} у.е.\n{50 * "-"}')
        log.append(f'Снято с депозита -{cash_extract} у.е. Баланс: {balance} у.е.')
        return action()
    else:
        print(f'Ввели неверную сумму. На вашем счёте: {Decimal(balance)} у.е.\n{50 * "-"}')
        return action()


def cash_machine_exit():
    global balance
    global counter
    return f'Завершение работы. На вашем счёте: {Decimal(balance)} у.е.\nОперации по счёту:\n{log}'


print(action())
