"""
3. Напишите функцию в шахматный модуль.
- Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
- Проверяйте различный случайные варианты и выведите 4 успешных расстановки
"""

__all__ = ['placement']

from random import randint as rni

ONE = 1
N = 8


def queens(x: list[int], y: list[int], n=N):
    for i in range(n):
        for j in range(i + ONE, n):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                return placement()
    return f'{x = }\n{y = }\n'


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
    return queens(x, y)


if __name__ == '__main__':
    for _ in range(4):
        print(placement())
        
