# Реализовать бинарный поиск элемента в отсортированном списке.
# Дан список чисел, пользователь вводит число, необходимо реализовать поиск
# введенного пользователем числа в этом списке с помощью бинарного поиска

def binary_search(lst, num):
    first = 0
    last = len(lst) - 1
    while first <= last:
        midlle: int = (first + last) // 2
        if lst[midlle] == num:
            return lst[midlle]
        elif lst[midlle] > num:
            last = midlle - 1
        else:
            first = midlle + 1
    return None

my_lst = [1, 10, 20, 22, 30, 85, 88, 99, 101]
print(binary_search(my_lst, 30))