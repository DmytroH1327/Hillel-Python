# Для списку цілих чисел потрібно знайти суму елементів із парними індексами [0-й, 2-й, 4-й ітд],
# потім перемножити цю суму на останній елемент вхідного масиву.
# Не забудьте, що перший елемент масиву має індекс 0.
# Для порожнього масиву результат завжди 0.
# Пояснення:
# [0, 1, 7, 2, 4, 8] => (0 + 7 + 4) * 8 = 88
# [1, 3, 5] => 30
# [6] => 36
# [] => 0

my_list = [0, 1, 7, 2, 4, 8]
# my_list = [1, 3, 5]
# my_list = [6]
# my_list = []

if not my_list:
    print(0)
else:
    list1 = [my_list[i] for i in range(0, len(my_list), 2)]
    new_list = sum(list1) * my_list[-1]
    print(new_list)
