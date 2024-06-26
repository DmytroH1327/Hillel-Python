# Користувач вводить рядок. Ваше завдання - перевірити, чи може цей рядок бути ім'ям змінної.
# Змінна не може:
#    починатися з цифри,
#    складатися тільки з цифр,
#    містити великі літери, пропуск і знаки пунктуації,
#    окрім нижнього підкреслення "_".
#    бути жодним із зареєстрованих слів.
# При цьому повне ім'я змінної може складатися тільки з одного нижнього підкреслення "_".
# Мається на увазі, що ПОВНЕ ім'я змінної може бути лише з одного символу "_" Більше одного не можна.
# Тобто якщо користувач ввів __ , то це вже помилка
# Якщо цей символ використовується для з'єднання слів в назві змінної - то таких символів може бути безліч
# У результаті перевірки на друк виводиться або True, якщо таке ім'я змінної допустимо, або False - якщо ні.

import keyword
import string

name = input("Введите имя переменной: ")

if name in keyword.kwlist or name[0] in string.digits or ' ' in name:
    print(False)
elif any(el.isupper() or el in string.punctuation for el in name if el != "_"):
    print(False)
elif name.count("__"):
    print(False)
else:
    print(True)
