"""
Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
данных), которые вы уже решали. Превратите функции в методы класса, а
параметры в свойства. Задачи должны решаться через вызов методов
экземпляра
"""

import csv
import json
import pickle
from pathlib import Path


class DirDictionary:
    def __init__(self, path):
        self.path = Path(path)

    def recursive2dict(self):
        all_files = self.path.glob('**/*')
        result = {}
        for file in all_files:
            if file.is_dir():
                f_type = 'directory'
                size = sum(file.stat(follow_symlinks=False).st_size for _ in file.rglob('*'))
            elif file.is_file():
                f_type = 'file'
                size = file.stat(follow_symlinks=False).st_size
            else:
                f_type = ''
                size = 0
            result[str(file)] = {"name": file.name, "f_type": f_type, "size": size, 'parent': str(file.parent)}

        with open('catalog.json', 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)

        with open('catalog.csv', 'w', encoding='utf-8') as f:
            wr = csv.writer(f, quoting=csv.QUOTE_ALL)
            wr.writerow(result)

        with open('catalog.pickle', 'wb') as f:
            pickle.dump(result, f, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
    rec = DirDictionary(Path.cwd())
    rec.recursive2dict()
