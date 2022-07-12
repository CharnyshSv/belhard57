# Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int

number = int(input('Число в десятичной СС: '))

numberb = ''

while number > 0:
    numberb = str(number % 2) + numberb
    number = number // 2

print(numberb)