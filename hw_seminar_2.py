"""
1. Напишите программу банкомат
- Начальная сумма равна нулю
- Допустимые действия: пополнить, снять, выйти
- Сумма пополнения и снятия кратны 50 у.е.
- Процент за снятие - 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
- После каждой третей операции пополнения или снятия начисляются проценты - 3%
- Нельзя снять больше, чем на счёте
- При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
- Любое действие выводит сумму денег
"""

from decimal import Decimal, getcontext

INITIAL_AMOUNT = 0
ZERO = 0
DIVISIBLE = 50
SERIAL_COUNT = 3
THREE_PERCENT = 1.03
EXTRACT_PERCENT = 0.015
MIN_FEE = 30
MAX_FEE = 600
RICHNESS = 5_000_000
RICHNESS_FEE = 0.1

count_deposit = 0
count_extract = 0
getcontext().prec = 10

while True:
    action = int(input('Введите требуемое действие:\n'
                       '1 - Пополнить счёт\n'
                       '2 - Снять наличные\n'
                       '3 - Выйти\n'
                       '-> '))
    if action == 1:
        cash_deposit = int(input('Внесите наличные кратные 50 у.е.: '))
        if Decimal(INITIAL_AMOUNT) >= RICHNESS:
            INITIAL_AMOUNT -= Decimal(INITIAL_AMOUNT) * Decimal(RICHNESS_FEE)
        if ZERO < cash_deposit and cash_deposit % DIVISIBLE == ZERO:
            count_deposit += 1
            INITIAL_AMOUNT += Decimal(cash_deposit)
            if count_deposit == SERIAL_COUNT:
                INITIAL_AMOUNT *= Decimal(THREE_PERCENT)
                count_deposit = ZERO
            print(f'На вашем счёте: {Decimal(INITIAL_AMOUNT)} у.е.', 50 * '-', sep='\n')
        else:
            print(f'Ввели неверную сумму. На вашем счёте: {Decimal(INITIAL_AMOUNT)} у.е.', 50 * '-', sep='\n')

    elif action == 2:
        cash_extract = int(input('Введите сумму для снятия кратные 50 у.е.: '))
        if Decimal(INITIAL_AMOUNT) >= RICHNESS:
            INITIAL_AMOUNT -= Decimal(INITIAL_AMOUNT) * Decimal(RICHNESS_FEE)
        if ZERO < cash_extract and cash_extract % DIVISIBLE == ZERO:
            count_extract += 1
            cash_extract_percent = cash_extract * EXTRACT_PERCENT
            if cash_extract_percent < MIN_FEE:
                INITIAL_AMOUNT -= Decimal(cash_extract - MIN_FEE)
            elif cash_extract_percent > MAX_FEE:
                INITIAL_AMOUNT -= Decimal(cash_extract - MAX_FEE)
            else:
                INITIAL_AMOUNT -= Decimal(cash_extract - cash_extract_percent)
            if INITIAL_AMOUNT < ZERO:
                print('Недостаточно средств на счёте!')
                continue
            if count_extract == SERIAL_COUNT:
                INITIAL_AMOUNT *= THREE_PERCENT
                count_extract = ZERO
            print(f'На вашем счёте: {Decimal(INITIAL_AMOUNT)} у.е.', 50 * '-', sep='\n')
        else:
            print(f'Ввели неверную сумму. На вашем счёте: {Decimal(INITIAL_AMOUNT)} у.е.', 50 * '-', sep='\n')
    elif action == 3:
        print(f'Завершение работы. На вашем счёте: {Decimal(INITIAL_AMOUNT)} у.е.')
        exit()
    else:
        print('Нет такого действия. Попытайтесь ещё', 50 * '-', sep='\n')

"""
2. Напишите программу, которая получает целое число и возвращает
его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата
"""

num = int(input('Введите число: '))
num_16 = ''
print(hex(num))

while num > 0:
    mid_num = num % 16
    if mid_num >= 10:
        match mid_num:
            case 10:
                num_16 += 'a'
            case 11:
                num_16 += 'b'
            case 12:
                num_16 += 'c'
            case 13:
                num_16 += 'd'
            case 14:
                num_16 += 'e'
            case 15:
                num_16 += 'f'
    else:
        num_16 += str(mid_num)
    num //= 16

print('0x' + num_16[::-1])

"""
3. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение дробей.
Для проверки своего кода используйте модуль fractions
"""

from fractions import Fraction
from math import gcd

a = input('Введите дробь 1 в формате "a/b": ')
b = input('Введите дробь 2 в формате "a/b": ')

# Проверка
print(f'Сложение: {Fraction(a) + Fraction(b)}. Умножение: {Fraction(a) * Fraction(b)}')

numerator_1 = int(a.split('/')[0])
numerator_2 = int(b.split('/')[0])
denominator_1 = int(a.split('/')[1])
denominator_2 = int(b.split('/')[1])

# Сложение дробей
if denominator_1 == denominator_2:
    numerator_sum = (numerator_1 + numerator_2) // gcd(numerator_1 + numerator_2, denominator_2)
    denominator_sum = denominator_1 // gcd(numerator_1 + numerator_2, denominator_2)
else:
    denominator_sum_mid = denominator_1 * denominator_2
    numerator_sum_mid = ((denominator_sum_mid // denominator_1 * numerator_1) + \
                     (denominator_sum_mid // denominator_2 * numerator_2))
    denominator_sum = denominator_sum_mid // gcd(numerator_sum_mid, denominator_sum_mid)
    numerator_sum = numerator_sum_mid // gcd(numerator_sum_mid, denominator_sum_mid)

# Умножение дробей
numerator_mult = numerator_1 * numerator_2 // gcd(numerator_1 * numerator_2, denominator_1 * denominator_2)
denominator_mult = denominator_1 * denominator_2 // gcd(numerator_1 * numerator_2, denominator_1 * denominator_2)

print(f'Сложение: {numerator_sum}/{denominator_sum}. Умножение: {numerator_mult}/{denominator_mult}')

