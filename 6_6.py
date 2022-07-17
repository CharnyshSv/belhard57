# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
# четные, потом нечётные

def sortedd(numbers: list) -> list:
    i = 0
    while i < len(numbers):
        if not numbers[i] % 2:
            numbers.insert(0, numbers.pop(i))
        else:
            i += 1

    return numbers

print(sortedd([1, 5, 2, 4, 2, 3, 6, 5, 9, 4, 5]))