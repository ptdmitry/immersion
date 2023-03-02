"""
Задание №5
Напишите функцию, которая ищет json файлы в указанной директории
и сохраняет их содержимое в виде одноимённых pickle файлов
"""

import pickle
import json
from pathlib import Path


def json2pickle(json_dir: Path):
    paths = Path(json_dir).glob('*.json')
    for path in paths:
        with open(path, 'r', encoding='utf-8') as f_json:
            json_file = json.load(f_json)
            with open(path.stem + '.pickle', 'wb') as f_pickle:
                pickle.dump(json_file, f_pickle)


if __name__ == '__main__':
    json2pickle(Path('files/'))
