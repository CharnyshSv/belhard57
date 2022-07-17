# Дан список чисел и на вход поступает число N, необходимо сместить список на
# указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]

def shift(numbers: list, n: int) -> list:
    if abs(n) > len(numbers):
        n -= (n // len(numbers)) * len(numbers)
    if n > 0:
        numbers = numbers[n:] + numbers[:n]
    else:
        numbers = numbers[-n:] + numbers[:-n]
    return numbers

numbers: list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n: int = int(input("enter number: "))

print(shift(numbers, n))

# можно упростить:

def shift_1(numbers: list, n: int) -> list:
    if abs(n) > len(numbers):
        n -= (n // len(numbers)) * len(numbers)
    numbers = numbers[n:] + numbers[:n]
    return numbers

numbers: list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#n: int = int(input("enter number: "))
#print(shift_1(numbers, n))