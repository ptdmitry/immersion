"""
Задание №2
Дорабатываем задачу 1
- Превратите внешнюю функцию в декоратор
- Он должен проверять входят ли переданные в функцию-угадайку числа
в диапазоны [1, 100] и [1, 10]
- Если не входят, вызывать функцию со случайными числами из диапазонов
"""

__all__ = ['guess_num']

from random import randint
from typing import Callable


def incoming_num(func: Callable):
    min_num = 1
    max_num = 100
    min_count = 1
    max_count = 10

    def wrapper(num: int, count: int, *args, **kwargs):
        if min_num > num or num > max_num:
            num = randint(min_num, max_num)
        if min_count > count or count > max_count:
            count = randint(min_count, max_count)
        result = func(num, count, *args, **kwargs)
        return result

    return wrapper


@incoming_num
def guess_num(num: int, count: int):
    for i in range(1, count + 1):
        print(f'Угадайте число. Попытка номер {i}')
        user_num = int(input('Введите число от 1 до 100: '))
        if user_num == num:
            print('Вы угадали')
            break
        elif user_num < num:
            print('Ваше число меньше загаданного')
        elif user_num > num:
            print('Ваше число больше загаданного')
    else:
        print('Попытки закончились ...')


guess_num(50, 5)
