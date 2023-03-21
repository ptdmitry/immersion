"""
Задание №5
Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы:
- загрузка данных (функция из задания 4)
- вход в систему - требует указать имя и id пользователя.
Для проверки наличия пользователя в множестве используйте
магический метод проверки на равенство пользователей.
Если такого пользователя нет, вызывайте исключение доступа.
А если пользователь есть, получите его уровень из множества пользователей
- добавление пользователя. Если уровень пользователя меньше,
чем ваш уровень, вызывайте исключение уровня доступа
"""

import json
from pathlib import Path
from task_13_6 import AccessError, LevelError


class User:
    def __init__(self, lvl, idx, name):
        self.lvl = lvl
        self.idx = idx
        self.name = name

    def __eq__(self, other):
        return self.idx == other.idx and self.name == other.name

    def __hash__(self):
        return hash((self.idx, self.name))

    def __repr__(self):
        return f'User(lvl={self.lvl}, idx{self.idx}, name={self.name})'


class Project:
    def __init__(self):
        self._users = set()
        self.me = None

    def read_json(self, file: Path) -> set[User]:
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for lvl, value in data.items():
            for idx, password in value.items():
                self._users.add(User(int(lvl), int(idx), password))
        return self._users

    def sign_in(self, name, idx):
        spam_user = User(name=name, idx=idx, lvl=0)
        if spam_user not in self._users:
            raise AccessError(name)
        print(f'Совпало. Пользователь "{name}" вошёл в систему')
        for user in self._users:
            if user == spam_user:
                self.me = user
                return user

    def user_add(self, name, idx, lvl):
        spam_user = User(name=name, idx=idx, lvl=lvl)
        if spam_user.lvl < self.me.lvl:
            raise LevelError(lvl)
        print(self._users)
        self._users.add(spam_user)
        print(self._users)
        return spam_user


if __name__ == '__main__':
    project = Project()
    res = project.read_json(Path('names.json'))
    # project.sign_in('Vasya', 2321)
    project.sign_in('Vasya', 232)
    project.user_add('Anton', 741, 1)
