# Калькулятор
a: int = int(input("Введите число 1: "))
b: int = int(input("Введите число 2: "))
operation = input("Введите знак (+, -, *. /): ")


if operation == "+":
    print(a+b)
elif operation == "-":
    print(a-b)
elif operation == "/":
    if b != 0:
        print(a/b)
    else:
        print('Деление на ноль!')
elif operation == "*":
    print(a*b)
else:
    print('Выберите верную операцию!')