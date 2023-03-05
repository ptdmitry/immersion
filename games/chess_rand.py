"""
3. Напишите функцию в шахматный модуль.
- Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
- Проверяйте различный случайные варианты и выведите 4 успешных расстановки
"""

__all__ = ['placement']

from random import randint as rni

ZERO = 0
ONE = 1
N = 8


def queens(x: list[int], y: list[int], n=N):
    res = True
    for i in range(n):
        for j in range(i + ONE, n):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                return False
    return True


def placement():
    x = []
    y = []
    while len(x) < N:
        rnd_x = rni(ONE, N)
        if rnd_x not in x:
            x.append(rnd_x)
    while len(y) < N:
        rnd_y = rni(ONE, N)
        if rnd_y not in y:
            y.append(rnd_y)
    return x, y


if __name__ == '__main__':
    idx = 4
    while idx > ZERO:
        x, y = placement()
        if queens(x, y):
            print(f'{x = }\n{y = }\n')
            idx -= ONE
            