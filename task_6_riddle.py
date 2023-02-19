"""
Задание №6
Добавьте в модуль с загадками функцию, которая принимает на вход строку
(текст загадки) и число (номер попытки, с которой она угадана)
- Функция формирует словарь с информацией о результатах отгадывания
- Для хранения используйте защищённый словарь уровня модуля
- Отдельно напишите функцию, которая выводит результаты угадывания
из защищённого словаря в удобном для чтения виде
- Для формирования результатов используйте генераторное выражение
"""

ZERO = 0
ONE = 1
TRIES = 3

__all__ = ['_get_guess', 'guess_dict']


def guess(question: str, answer: list[str], tries: int):
    count = ZERO
    while count < tries:
        user_answer = input(f'Угадай загадку за {tries - count} попытки! {question}: ').lower()
        count += ONE
        if user_answer in answer:
            # return count
            return _get_guess(question, count)
    # return 0
    return _get_guess(question, ZERO)


def guess_dict(func, count=TRIES):
    data = {
            'Висит груша, нельзя скушать': ['люстра', 'лампа', 'лампочка'],
            'Зимой и летом одним цветом': ['ель', 'ёлка', 'елка', 'сосна', 'солдат'],
            'Шапочка для лампочки': ['бра', 'абажур'],
            'Конь бежит, земля дрожит': ['гром', 'гроза']
            }
    for key, value in data.items():
        print(func(key, [el.lower() for el in value], count))
    return 'Game Over!'


def _get_guess(guess_text: str, guess_tries: int):
    get_guess_dict = {guess_text: guess_tries}
    return results(get_guess_dict)


def results(res: dict):
    for key, value in res.items():
        if value == ZERO:
            return f'Загадка "{key}" не отгадана\n'
        else:
            return f'Загадка "{key}" отгадана с попытки {value}\n'


if __name__ == '__main__':
    print(guess_dict(guess))
