"""
1. Напишите функцию группового переименования файлов. Она должна:
- принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер
- принимать параметр количество цифр в порядковом номере
- принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога
- принимать параметр расширение конечного файла
- принимать диапазон сохраняемого оригинального имени.
Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение

Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами
"""

from pathlib import Path


def rename_files(name: str, count: int, ext_before: str, ext_after: str, letter_range: list[int]):
    p = (Path.cwd() / 'DIR_TEST').glob(f'*.{ext_before}')
    print(p)
    count_range = 0
    for obj in p:
        if obj.is_file():
            count_range += 1
            new_name = f'{obj.stem[letter_range[0]:letter_range[1]]}{name}_{str(count_range).zfill(count)}.{ext_after}'
            new_name = Path(Path.cwd() / 'DIR_TEST', new_name)
            obj.replace(new_name)


if __name__ == '__main__':
    rename_files(name='new_name_file', count=3, ext_before='txt', ext_after='md', letter_range=[2, 4])
