"""
Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
Напишите к ним классы исключения с выводом подробной информации.
Поднимайте исключения внутри основного кода.
Например нельзя создавать прямоугольник со сторонами отрицательной длины
"""
from figure_exception import ZeroNegativeLenError, TypeValueError


class Rectangle:
    def __init__(self, length, width=None):
        if not isinstance(length, (int | float)):
            raise TypeValueError(length)
        elif length <= 0:
            raise ZeroNegativeLenError(length)
        self.length = length
        if width is not None and not isinstance(width, (int | float)):
            raise TypeValueError(width)
        elif width <= 0:
            raise ZeroNegativeLenError(width)
        self.width = width if width is not None else length

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length + self.width) * 2

    def __add__(self, other):
        new_perimeter = self.perimeter() + other.perimeter()
        new_width = self.width + other.width
        new_length = new_perimeter / 2 - new_width
        return Rectangle(new_width, new_length)

    def __sub__(self, other):
        new_perimeter = abs(self.perimeter() - other.perimeter())
        new_width = abs(self.width - other.width)
        new_length = new_perimeter / 2 - new_width
        return Rectangle(new_width, new_length)


if __name__ == '__main__':
    r1 = Rectangle(8, -4)
    r2 = Rectangle('8', -4)
