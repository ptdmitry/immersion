"""
Добавьте ко всем задачам с семинара строки документации и методы вывода
информации на печать
"""


class Rectangle:
    """
    Класс Rectangle, в котором добавлена возможность сложения и вычитания периметров прямоугольников.
    При этом должен создаётся новый экземпляр прямоугольника.
    При вычитании не допускается отрицательных значений.
    """
    def __init__(self, length, width=None):
        """Инициализация свойств экземпляра класса Rectangle."""
        self.length = length
        self.width = width if width is not None else length

    def area(self):
        """Метод расчёта площади прямоугольника."""
        return self.length * self.width

    def perimeter(self):
        """Метод расчёта периметра прямоугольника."""
        return (self.length + self.width) * 2

    def __add__(self, other):
        """Метод расчёта суммы периметров складываемых прямоугольников."""
        new_perimeter = self.perimeter() + other.perimeter()
        new_width = self.width + other.width
        new_length = new_perimeter / 2 - new_width
        return Rectangle(new_width, new_length)

    def __sub__(self, other):
        """
        Метод расчёта разности периметров вычитаемых прямоугольников.
        Предусмотрено, что невозможно получение отрицательных значенний.
        """
        new_perimeter = abs(self.perimeter() - other.perimeter())
        new_width = abs(self.width - other.width)
        new_length = new_perimeter / 2 - new_width
        return Rectangle(new_width, new_length)


if __name__ == '__main__':
    r1 = Rectangle(2)
    print(r1.perimeter())
    r2 = Rectangle(4, 5)
    print(r2.perimeter())
    r3 = r1 + r2
    print(r3.perimeter())
    print(f'{r1 = }')
    print(f'{r3 = }')
    r3 = r1 - r2
    print(r3.perimeter())
    print(f'{r1 = }')
    print(f'{r3 = }')
