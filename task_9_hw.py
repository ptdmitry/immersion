"""
Напишите следующие функции:
- Нахождение корней квадратного уравнения
- Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк
- Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла
- Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл
Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса
"""

import csv
import json
from math import sqrt
from random import randint
from typing import Callable

ZERO = 0


def gen_csv():
    min_num = -1000
    max_num = 1000
    min_count = 100
    max_count = 1000
    with open('numbers.csv', 'w', encoding='utf-8', newline='') as f_csv:
        csv_file = csv.DictWriter(f_csv, fieldnames=['a', 'b', 'c'],
                                  dialect='excel', quoting=csv.QUOTE_MINIMAL)
        csv_file.writeheader()
        rnd_str = randint(min_count, max_count)
        for i in range(rnd_str):
            rows = []
            for j in range(3):
                rows.append({'a': randint(min_num, max_num),
                             'b': randint(min_num, max_num),
                             'c': randint(min_num, max_num)})
            csv_file.writerows(rows)


def numbers_csv(func: Callable):
    def wrapper(*args, **kwargs):
        with open('numbers.csv', 'r', encoding='utf-8') as f_csv:
            csv_file = list(csv.reader(f_csv, dialect='excel'))[1:]
        result = func(csv_file, *args, **kwargs)
        return result
    return wrapper


def results2json(func: Callable):
    json_file = []

    def wrapper(*args, **kwargs):
        json_dict = {}
        result = func(*args, **kwargs)
        for key, value in result.items():
            json_dict[key] = value
        json_file.append(json_dict)
        with open('results_equation.json', 'w', encoding='utf-8') as f_json:
            json.dump(json_file, f_json, indent=2)
        return result
    return wrapper


@results2json
@numbers_csv
def equation(num_list):
    results = {}
    for line in num_list:
        a, b, c = int(line[0]), int(line[1]), int(line[2])
        if a == ZERO:
            continue
        discriminant = b ** 2 - 4 * a * c
        if discriminant > 0:
            x1 = (-b + sqrt(discriminant)) / (2 * a)
            x2 = (-b - sqrt(discriminant)) / (2 * a)
            results[f'{a = }, {b = }, {c = }'] = f'{discriminant = }, {x1 = :.2f}, {x2 = :.2f}'
        elif discriminant == 0:
            x = -b / (2 * a)
            results[f'{a = }, {b = }, {c = }'] = f'{discriminant = }, {x = :.2f}'
        else:
            results[f'{a = }, {b = }, {c = }'] = 'No roots'
    return results


gen_csv()
equation()
