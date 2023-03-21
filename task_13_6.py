"""
Задание №6
Доработайте классы исключения так, чтобы они выдали
подробную информацию об ошибках
- Передавайте необходимые данные из основного кода проекта
"""


class ProjectException(Exception):
    pass


class LevelError(ProjectException):
    def __init__(self, lvl):
        self.lvl = lvl

    def __str__(self):
        return f'Невозможно добавить пользователя. Ваш уровень ниже уровня "{self.lvl}"'


class AccessError(ProjectException):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Такого пользователя "{self.name}" нет в системе. В доступе отказано'



# class UserAgeError(UserException):
#     def __init__(self, value):
#         self.value = value
#
#     def __str__(self):
#         return f'Возраст пользователя должен быть целым int() или вещественным float() больше ноля\n' \
#                f'У вас тип {type(self.value)}, а значение {self.value}'
#
#
# class UserNameError(UserException):
#     def __init__(self, name, lower, upper):
#         self.name = name
#         self.lower = lower
#         self.upper = upper
#
#     def __str__(self):
#         text = 'попадает в'
#         if len(self.name) < self.lower:
#             text = 'меньше нижней'
#         elif len(self.name) > self.lower:
#             text = 'больше верхней'
#         return f'Имя пользователя {self.name} содержит {len(self.name)} символа(ов).\n' \
#                f'Это {text} границы. Попадите в диапазон ({self.lower}, {self.upper}).'