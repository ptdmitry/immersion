"""
Напишите функцию, которая получает на вход директорию и рекурсивно
обходит её и все вложенные директории. Результаты обхода сохраните в
файлы json, csv и pickle
- Для дочерних объектов указывайте родительскую директорию
- Для каждого объекта укажите файл это или директория
- Для файлов сохраните его размер в байтах, а для директорий размер
файлов в ней с учётом всех вложенных файлов и директорий
- Соберите из созданных на уроке и в рамках домашнего задания функций
пакет для работы с файлами разных форматов
"""

import csv
import json
import pickle
from pathlib import Path


def recursive2dict(direct: Path) -> None:
    all_files = Path(direct).glob('**/*')
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
    recursive2dict(Path('files/files_task_8_hw'))
