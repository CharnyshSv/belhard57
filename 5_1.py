# Вывести N первых чисел кратные M и больше K
N: int = int(input("Enter number: "))
M: int = int(input("Enter number: "))
K: int = int(input("Enter number: "))

while N:
    if K % M == 0:
        print(K)
        N -= 1
    K += 1