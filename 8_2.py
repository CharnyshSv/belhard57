# Вывести в порядке возрастания цифры, входящие в десятичную запись натурального числа N.
N = int(input('Введите N: '))


def sortedd_numbers(N):
    numbers = str(N)
    numbers = "".join(sorted(numbers))
    return numbers

print(sortedd_numbers(N))

