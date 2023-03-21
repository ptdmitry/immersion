class FigureException(Exception):
    pass


class ZeroNegativeLenError(FigureException):
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f'Прямоугольника не существует со стороной = {self.side}'


class TypeValueError(FigureException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Неверный формат значения "{type(self.value)}".\n' \
               f'Введите значение формата "int" или "float"'
