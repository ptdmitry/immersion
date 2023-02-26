"""
Дорабатываем функции из предыдущих задач
- Генерируйте файлы в указанную директорию - отдельный параметр функции
- Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки)
- Существующие файлы не должны удаляться/изменяться в случае совпадения имён
"""

from make_files import make_files
from pathlib import Path
from os import chdir

COUNT_FILES = 5


def make_dir(func, dir_name: Path):
    if not Path.exists(dir_name):
        Path(f'{dir_name}').mkdir()
    chdir(dir_name)
    func('txt', count=COUNT_FILES)


if __name__ == '__main__':
    make_dir(make_files, Path('DIR_TEST'))
