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

    def __eq__(self, other):
        """
        Метод сравнения периметров прямоугольников.
        Если периметры равны, то вернётся 'True',
        в противном случае вернётся 'False'
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Метод сравнения периметров прямоугольников.
        Если периметры не равны, то вернётся 'True',
        в противном случае вернётся 'False'
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Метод сравнения периметров прямоугольников.
        Если периметр первого прямоугольника больше, чем периметр второго,
        то вернётся 'True', в противном случае вернётся 'False'
        """
        return self.area() > other.area()

    def __lt__(self, other):
        """
        Метод сравнения периметров прямоугольников.
        Если периметр первого прямоугольника меньше, чем периметр второго,
        то вернётся 'True', в противном случае вернётся 'False'
        """
        return self.area() < other.area()

    def __ge__(self, other):
        """
        Метод сравнения периметров прямоугольников.
        Если периметры первого прямоугольника больше или равен периметру второго,
        то вернётся 'True', если меньше - вернётся 'False'
        """
        return self.area() >= other.area()

    def __le__(self, other):
        """
        Метод сравнения периметров прямоугольников.
        Если периметры первого прямоугольника меньше или равен периметру второго,
        то вернётся 'True', если больше - вернётся 'False'
        """
        return self.area() <= other.area()


if __name__ == '__main__':
    r1 = Rectangle(2)
    print(r1.perimeter())

    print(r1 == Rectangle(1, 4))
    print(r1 != Rectangle(1, 4))
    print(r1 > Rectangle(1, 4))
    print(r1 < Rectangle(1, 4))
    print(r1 >= Rectangle(1, 4))
    print(r1 <= Rectangle(1, 4))
