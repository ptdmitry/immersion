"""
Доработаем задачи 5-6. Создайте класс-фабрику
- Класс принимает тип животного (название одного из созданных классов)
и параметры для этого типа
- Внутри класса создайте экземпляр на основе переданного типа и
верните его из класса-фабрики
"""

class MakeAnimal:
    def __init__(self, animal, *args):
        self.animal = animal.lower()
        self.args = args

    def get_animal(self):
        if self.animal == 'dog':
            d = Dog(*self.args)
            return d.get_height()
        elif self.animal == 'fish':
            f = Fish(*self.args)
            return f.get_color()
        elif self.animal == 'bird':
            b = Bird(*self.args)
            return b.can_flies()


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Fish(Animal):
    def __init__(self, color, name, age):
        self.color = color
        super().__init__(name, age)

    def get_color(self):
        return f'Цвет рыбы {self.name} - {self.color}'


class Bird(Animal):
    def __init__(self, is_flies, *args):
        self.is_flies = is_flies
        super().__init__(*args)

    def can_flies(self):
        return f'Птица {self.name} умеет летать? {self.is_flies}!'


class Dog(Animal):
    def __init__(self, height, *args):
        self.height = height
        super().__init__(*args)

    def get_height(self):
        if self.height < 0.5:
            return f'{self.name} маленький собачонок'
        elif 0.5 < self.height < 1:
            return f'{self.name} обычная собака'
        else:
            return f'Собака {self.name} в холке {self.height} метров! Большая собака!'


if __name__ == '__main__':
    ma1 = MakeAnimal('DOG', 1, 'Рекс', 4)
    print(ma1.get_animal())
    ma2 = MakeAnimal('bird', True, 'ворона', 1)
    print(ma2.get_animal())
    ma3 = MakeAnimal('fish', 'красный', 'Рыбец', 1)
    print(ma3.get_animal())
