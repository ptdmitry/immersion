"""
1. Три друга взяли вещи в поход. Сформируйте словарь, где ключ - имя друга,
а значение - кортеж вещей. Ответьте на вопросы:
- какие вещи взяли все три друга
- какие вещи уникальны, есть только у одного друга
- какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
Для решения используйте операции с множествами.
Код должен расширяться на любое большее количество друзей
"""

friends_dict = {'Alex': ('knife', 'glass', 'socks', 'plate', 'spoon', 'backpack'),
                'Vasya': ('match', 'bucket', 'cap', 'plate', 'spoon', 'backpack', 'tent'),
                'Petya': ('sleeping_bag', 'glass', 'socks', 'plate', 'fork', 'bag'),
                'Egor': ('axe', 'cup', 'socks', 'plate', 'spoon', 'backpack', 'tent')}

ZERO = 0
ONE = 1

all_things = {}
uniq_thing = set()

for key, value in friends_dict.items():
    for thing in value:
        all_things[thing] = all_things.setdefault(thing, ZERO) + ONE

for key, value in all_things.items():
    if value == ONE:
        uniq_thing.add(key)

for key, val in all_things.items():
    if val == len(friends_dict) - 1:
        for name, things in friends_dict.items():
            if key not in things:
                print(f"Only {name} didn't take {key}")

print(f'{all_things = }')
print(f'{uniq_thing = }')

"""
2. Дан список повторяющихся элементов. 
Вернуть список с дублирующимися элементами. 
В результирующем списке не должно быть дубликатов
"""

some_list = [1, 2, 7, 4, 9, 3, 2, 6, 1, 7, 6, 5, 4, 2, 1, 9, 10, 54]
ONE = 1
res_list = set()

for num in some_list:
    if some_list.count(num) > ONE:
        res_list.add(num)
print(list(res_list))

"""
3. В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
Не учитывать знаки препинания и регистр символов. 
За основу возьмите любую статью из википедии или из документации к языку
"""

article = """ Python uses dynamic typing and a combination of reference counting
and a cycle-detecting garbage collector for memory management.
It uses dynamic name resolution (late binding),
which binds method and variable names during program execution.
Its design offers some support for functional programming in the Lisp tradition.
It has filter,mapandreduce functions; list comprehensions, dictionaries, sets, and generator expressions.
The standard library has two modules (itertools and functools) that
implement functional tools borrowed from Haskell and Standard ML.

Its core philosophy is summarized in the document The Zen of Python (PEP 20), which includes aphorisms such as:

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Readability counts.
Rather than building all of its functionality into its core,
Python was designed to be highly extensible via modules.
This compact modularity has made it particularly popular as a means
of adding programmable interfaces to existing applications.
Van Rossum's vision of a small core language with a large standard library
and easily extensible interpreter stemmed from his frustrations with ABC,
which espoused the opposite approach.

Python strives for a simpler, less-cluttered syntax and grammar
while giving developers a choice in their coding methodology.
In contrast to Perl's "there is more than one way to do it" motto,
Python embraces a "there should be one—and preferably only one—obvious way to do it" philosophy.
Alex Martelli, a Fellow at the Python Software Foundation and Python book author, wrote:
"To describe something as 'clever' is not considered a compliment in the Python culture." """.replace('"', '')\
    .replace('.', '').replace(',', '').replace(')', '').replace('(', '').replace(':', '')\
    .replace(';', '').replace("'", "").split()

ZERO = 0
ONE = 1
LIMIT = 10
words_dict = {}
sorted_words_dict = {}

for word in article:
    words_dict[word] = words_dict.setdefault(word, ZERO) + ONE

sorted_keys = sorted(words_dict, key=words_dict.get, reverse=True)[:LIMIT]

for key in sorted_keys:
    sorted_words_dict[key] = words_dict[key]

print(sorted_words_dict)

"""
4. Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
Достаточно вернуть один допустимый вариант
*Верните все возможные варианты комплектации рюкзака
"""

things = {'tent': 3, 'sleeping_bag': 2, 'axe': 1, 'bucket': 1, 'potato': 5, 'carrot': 2, 'buckwheat': 2}
BACKPACK_LIMIT = 10
ZERO = 0

keys = tuple(things.keys())
for i in range(len(keys)):
    for j in range(i, len(keys)):
        weight_max = (*keys[:i], keys[j])
        weight_value = 0
        for item in weight_max:
            weight_value += things[item]
        if weight_value <= BACKPACK_LIMIT:
            print(f"Can take in backpack {weight_max}, total weight {weight_value} kg")
