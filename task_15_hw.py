"""
Возьмите любые 1-3 задачи из прошлых домашних заданий.
Добавьте к ним логирование ошибок и полезной информации.
Также реализуйте возможность запуска из командной строки с передачей параметров
"""

from string import ascii_letters
import logging
import argparse

FORMAT = '{levelname} - {asctime} - {funcName} - {msg}'
logging.basicConfig(filename="text_filter.log", encoding='utf-8',
                    level=logging.INFO, style='{', format=FORMAT)
logger = logging.getLogger(__name__)


def text_filter(string: str) -> str:
    result = ''.join(char for char in string if char in set(ascii_letters + ' '))
    logger.info(f"In: {string}. Out: {result}")
    return result.lower()


def get_parser():
    parser = argparse.ArgumentParser(description='Удаление из текста всех символов '
                                                 'кроме букв латинского алфавита и пробелов')
    parser.add_argument('-s', '--string', default='Empty string! Ничего не ввели!')
    args = parser.parse_args()
    return text_filter(args.string)


print(get_parser())
