#Дан список чисел, необходимо его развернуть без использования метода revese и
# функции reversed, а так же дополнительного списка и среза


def reverse_lst(x):
    return x[::-1]

x =[1, 2, 3, 4, 5]

y = reverse_lst(x)

print(y)