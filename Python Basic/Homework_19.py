# Напишіть функцію common_elements, яка згенерує два списки елементів .
# Один список з числами кратними 3, інший з кратними числами 5.
# Кількість елементів у цих списках може бути різним.
# За допомогою множин створіть набір з числами, які є в обох множинах (перетин).
# Функція повинна повернути цю множину як результат своєї роботи.

import random

def common_elements():
    lst_a = []
    lst_b = []

    size_a = random.randrange(1, 99)
    size_b = random.randrange(1, 99)

    for _ in range(size_a):
        lst_a.append(random.randrange(3, 99, 3))
    for _ in range(size_b):
        lst_b.append(random.randrange(5, 99, 5))

    set_a = set(lst_a)
    set_b = set(lst_b)
    intersection_set = set_a.intersection(set_b)

    return intersection_set

print(common_elements())
