"""
Задание №6
Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл
- Для тестированию возьмите pickle версию файла из задачи 4 этого семинара
- Функция должна извлекать ключи словаря для заголовков столбца из переданного файла
"""

import pickle
import csv
from pathlib import Path


def pickle2csv(file_out: Path, file_in: Path) -> None:
    with open(file_out, 'rb') as f_pickle:
        user_dict = pickle.load(f_pickle)

    rows = []
    for level, value in user_dict.items():
        rows.append({'level': level, 'value': value})
        for id, name in value.items():
            rows.append({'id': id, 'name': name})
    # print(rows)
    with open(file_in, 'w', newline='', encoding='utf-8') as f_csv:
        fieldnames = ['level', 'value', 'id', 'name']
        writer = csv.DictWriter(f_csv, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == '__main__':
    pickle2csv(Path('files/user_info.pickle'), Path('files/user_info.csv'))
