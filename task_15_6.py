"""
Задание №6
Напишите код, который запускается из командной строки
и получает на вход путь до директории на ПК.
Соберите информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит:
- имя файла без расширения или название каталога,
- расширение, если это файл,
- флаг каталога,
- название родительского каталога
"""

import argparse
import os
from pathlib import Path
from collections import namedtuple
import logging

logging.basicConfig(filename="tracker.log", encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)


def get_files(directory: Path):
    Object = namedtuple('Object', 'object_name, extension, catalog_flag, parent_dir')
    all_files = Path(directory).glob('*')
    for file in all_files:
        if file.is_file():
            file_name = file.name.split('.')[0]
            extension = f".{file.name.split('.')[1]}" if str(file.name).count('.') == 1 else None
            catalog_flag = (os.stat(file).st_mode & 0o777)
            parent_dir = str(file.parent).split('\\')[-1]
            to_write = Object._make([file_name, extension, catalog_flag, parent_dir])
            logger.info(to_write)
        elif file.is_dir():
            file_name = file.name
            extension = None
            catalog_flag = (os.stat(file).st_mode & 0o777)
            parent_dir = str(file.parent).split('\\')[-1]
            to_write = Object._make([file_name, extension, catalog_flag, parent_dir])
            logger.info(to_write)


def get_parser():
    parser = argparse.ArgumentParser(description='Содержимое указанной папки')
    parser.add_argument('-p', '--path', default=Path(os.getcwd()))
    args = parser.parse_args()
    directory = Path(input("Введите путь до папки: "))
    path = directory if directory.is_dir() else args.path
    return get_files(path)


if __name__ == '__main__':
    get_parser()
