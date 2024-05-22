# Користувач вводить через дефіс дві літери, Ваше завдання написати програму,
# яка повертатиме всі символи між ними включно.
# Жодних перевірок на помилку робити не треба, мінімальне значення завжди менше або дорівнює максимальному.
# Приклад:
# "a-c" -> abc
# "a-a" -> a
# "s-H" -> stuvwxyzABCDEFGH
# "a-A" -> abcdefghijklmnopqrstuvwxyzA

import string

letter = input("Введите две буквы через дифис (a-c): ")

abc = string.ascii_letters
x, y = letter[0], letter[2]
index_start = abc.find(x)
index_end = abc.find(y)

letters = abc[index_start:index_end + 1]
print(letters)