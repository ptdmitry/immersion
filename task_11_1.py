"""
Добавьте ко всем задачам с семинара строки документации и методы вывода
информации на печать
"""

from time import time


class MyStr(str):
    """
    Класс Моя Строка, где доступны все возможности str
    дополнительно хранятся имя автора строки и время создания (time.time).
    """
    def __new__(cls, value, author):
        """Расширение класса str."""
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = time()
        return instance

    def __str__(self):
        """Метод представления экземпляра класса MyStr для для пользователя."""
        return f'Строка {self!r} написана автором {self.author}'


if __name__ == '__main__':
    help(MyStr)
    # s = MyStr('Hello world!', 'prepod')
    # print(s)
    # print(s.author)
    # s2 = MyStr('Hi', 'student')
    # print(s2.author)
    # print(s.upper())
