"""
Задание №7
Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader
- Распечатайте его как pickle строку
"""

import pickle
import csv
from pathlib import Path


def csv2pickle(file_out: Path) -> bytes:
    users_lst = []
    with open(file_out, 'r', encoding='utf-8') as f_csv:
        reader = csv.reader(f_csv)
        for i, row in enumerate(reader):
            if i == 0:
                continue
            users_dict = {}
            level, value, id, name = row
            if level == '':
                users_dict['level'] = level
            else:
                users_dict['level'] = int(level)
            users_dict['value'] = value
            users_dict['id'] = id.zfill(10)
            users_dict['name'] = name.title()
            users_dict['hash'] = hash(f'{id}{name}')
            users_lst.append(users_dict)
    res = pickle.dumps(users_lst, protocol=pickle.DEFAULT_PROTOCOL)
    return res


if __name__ == '__main__':
    print(csv2pickle(Path('files/user_info.csv')))
