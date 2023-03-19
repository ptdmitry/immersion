"""
Создайте класс студента
- Используя дескрипторы проверяйте ФИО на
первую заглавную букву и наличие только букв
- Названия предметов должны загружаться из файла CSV
при создании экземпляра. Другие предметы в экземпляре недопустимы
- Для каждого предмета можно хранить оценки (от 2 до 5)
и результаты тестов (от 0 до 100)
- Также экземпляр должен сообщать средний балл по тестам
для каждого предмета и по оценкам всех предметов вместе взятых
"""
from pathlib import Path
import csv
from random import randint


def csv_creator():
    file = Path(f'subjects.csv')
    fieldnames = ['Предмет', 'Оценка', 'Результат теста']
    subjects = ['Математика', 'Литература', 'Физика']
    marks = [(randint(2, 5) for _ in range(randint(2, 10))) for _ in range(5)]
    test_results = [(randint(0, 100) for _ in range(randint(2, 10))) for _ in range(5)]
    rows = []

    for subject, mark, test in zip(subjects, marks, test_results):
        rows.append([subject, [*mark], [*test]])

    with open(file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(fieldnames)
        for subj_row in rows:
            writer.writerow(subj_row)

    return f


def csv_reader(file: Path):
    subjects = []
    test_results = {}
    marks = {}
    csv_creator()
    with open(file.name, 'r', encoding='utf-8') as f:
        data = list(csv.reader(f))[1:]
    for row in data:
        subjects.append(row[0])
        for i in row[1]:
            if i.isdigit():
                marks.setdefault(row[0], []).append(int(i))
        for j in row[2]:
            if j.isdigit():
                test_results.setdefault(row[0], []).append(int(j))
    return [subjects, marks, test_results]


class NameDescriptor:
    def __init__(self, name: str = None):
        self.name = name

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if not value.istitle():
            raise TypeError(f'Имя (фамилия) должны начинаться с заглавной буквы')
        if not value.isalpha():
            raise TypeError(f'В имени (фамилии) не должно быть чисел')


class Student:
    first_name = NameDescriptor()
    last_name = NameDescriptor()

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.__test_results = None
        self.__marks = None
        self.file = Path('subjects.csv')
        self.__file = csv_reader(self.file)
        self.__subjects = csv_reader(self.file)[0]

    def test_calcs(self):
        self.__test_results = self.__file[2]
        avg_tests = {}

        for subject, marks in self.__test_results.items():
            avg_tests.setdefault(subject, 0)
            avg_tests[subject] = f'{(sum(marks) / len(marks)):.2f}'

        return avg_tests

    def marks_calcs(self):
        self.__marks = self.__file[1]
        nums = []
        for marks in self.__marks.values():
            for i in marks:
                nums.append(i)
        avg_total = f'{(sum(nums) / len(nums)):.2f}'
        return avg_total

    def __str__(self):
        return f'Студент: {self.first_name} {self.last_name}\n' \
               f'Предметы: {self.__subjects}\n' \
               f'Средний балл по тестам: {self.test_calcs()}\n' \
               f'Средний балл по предметам вместе взятых: {self.marks_calcs()}'


if __name__ == '__main__':
    std_one = Student('Архимед', 'Иванович')
    print(std_one)
    # std_two = Student('Аристотель', 'Джонович3')
    # std_three = Student('Аристотель', 'джонович')
