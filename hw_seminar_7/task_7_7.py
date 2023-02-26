"""
Задание №7
Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
- Каждая группа включает файлы с несколькими расширениями
- В исходной папке должны остаться только те файлы, которые не подошли для сортировки
"""
import shutil
from pathlib import Path


def sort_files(path: Path):
    lst_files = Path(path)
    files_dict = {'pictures': ['png', 'jpg', 'jpeg', 'gif'],
                  'videos': ['mp4', 'avi', 'mkv', 'mov'],
                  'documents': ['txt', 'pdf', 'doc'],
                  'music': ['mp3', 'wav', 'm3u', 'flac']}
    for obj in lst_files.iterdir():
        for key, value in files_dict.items():
            if obj.is_file() and str(obj).split('.')[-1] in value:
                if not Path.exists(Path(f'D:\\FILES\\{key}')):
                    Path(f'D:\\FILES\\{key}').mkdir()
                shutil.move(f'{obj}', f'D:\\FILES\\{key}')


if __name__ == '__main__':
    p = 'D:\\FILES'
    sort_files(Path(p))
