# Вывести четные числа от 2 до N по 5 в строку
N: ini = int(input('Введите N: '))
c = 0
for i in range(2, N+1, 2):
    if c < 5:
        c += 1
    else:
        c = 1
        print()
    print(i, end=" ")
