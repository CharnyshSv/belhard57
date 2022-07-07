# Заполнить список степенями числа 2 (от 2^1 до 2^n)
n: int = int(input('Enter number'))  # любое число
#range(int(n))
numbers: list[int] = [2 ** i for i in range(n)]
print(numbers)
