"""
Задание №7
Создайте функцию-генератор
- Функция генерирует N простых чисел, начиная с числа 2
- Для проверки числа на простоту используйте правило:
“число является простым, если делится нацело только на единицу и на себя”
"""


def simple_nums_gen(n):
    simple_num = 2
    count = 0
    while count < n:
        for i in range(2, simple_num):
            if (simple_num % i) == 0:
                break
        else:
            count += 1
            yield simple_num
        simple_num += 1


num = int(input('Сколько сгенерировать простых чисел? '))
for i in simple_nums_gen(num):
    print(i)

"""
2. Напишите функцию, которая принимает на вход строку - абсолютный путь до
файла. Функция возвращает кортеж из трёх элементов: путь, имя файла,
расширение файла
"""


def parce(link):
    link_lst = link.split('/')
    return '/'.join(link_lst[2:-1]), *link_lst[-1].split('.')[-2:-1], *link_lst[-1].split('.')[-1:]


res = parce('https://hb.bizmrg.com/frontend-scripts/assets/Widgets-2022/widebanner-new_desktop.png')
print(res)

"""
3. Напишите однострочный генератор словаря, который принимает на вход три
списка одинаковой длины: имена str, ставка int, премия str с указанием
процентов вида “10.25%”. В результате получаем словарь с именем в качестве
ключа и суммой премии в качестве значения. Сумма рассчитывается как
ставка умноженная на процент премии
"""

names = ['Egor', 'Andrey', 'Dmitry']
bet = [52_000, 35_000, 52_000]
bonus = ['25%', '45%', '25%']


def salary_gen(names, bet, bonus):
    return {i: j + j * int(k.replace('%', '')) // 100 for k in bonus for j in bet for i in names}


res = salary_gen(names, bet, bonus)
print(res)

"""4. Создайте функцию генератор чисел Фибоначчи (см. Википедию)"""


def fib(n):
    number = 0
    idx = 1
    for i in range(n):
        yield number
        number, idx = idx, number + idx


for i in fib(20):
    print(i, end=' ')
