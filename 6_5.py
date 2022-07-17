#Дан список чисел, необходимо его развернуть без использования метода revese и
# функции reversed, а так же дополнительного списка и среза


#def reverse_lst(x):
#   return x[::-1]

#x =[1, 2, 3, 4, 5]

#y = reverse_lst(x)

#print(y)

# решение без среза ()
# ~ тильда, формула -(i+1)

def rev(lst: list) -> list:
    for i in range(len(lst) // 2):
        lst[i], lst[~i] = lst[~i], lst[i]
    return lst

print(rev([1, 2, 3, 4]))