# Модифікувати калькулятор (Homework_4) таким чином, щоб він працював доти, доки користувач цього хоче

start_calculator = "yes"

while start_calculator.lower() == "yes":
    a = int(input("Введите число A: "))
    b = int(input("Введите число B: "))
    c = input("Введите операцию (+, -, *, /): ")
    if c == "+":
        print(a, "+", b, "=", a + b)
    elif c == "-":
        print(a, "-", b, "=", a - b)
    elif c == "*":
        print(a, "*", b, "=", a * b)
    elif c == "/":
        if b == 0:
            print("Делитель не должен быть нулем!")
        else:
            print(a, "/", b, "=", a / b)
    start_calculator = input("Продолжить работу калькулятора? (Yes/No): ")
    if start_calculator.lower() == "yes":
        continue
    else:
        break
