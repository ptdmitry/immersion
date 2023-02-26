from random import randint, choices
from string import ascii_letters, digits
from pathlib import Path


def make_files(extension: str, min_name: int = 6, max_name: int = 38,
               min_size: int = 256, max_size: int = 4096, count: int = 42):
    for _ in range(count):
        name = ''.join(choices(ascii_letters+digits, k=randint(min_name, max_name)))
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
        if Path(f'{name}.{extension}').exists():
            print(f'Файл {name}.{extension} существует')
        with open(f'{name}.{extension}', 'xb') as f:
            f.write(data)


if __name__ == '__main__':
    make_files('txt', count=5)
