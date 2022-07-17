# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка
# незаконно
from typing import List

list = [1, 10, 'pp', True, 'hello', 'a', 3, False, None]


def filter_terms(lst: list) -> list:
    list = [i for i in lst if isinstance(i, str)]
    return list


#print(filter_terms(list))

# второй способ

def str_sorted(lst: list) -> list:
#    return lst = list(filter(lambda x: isinstance(x, str), lst))
    i = 0
    while i < len(lst):
        if not isinstance(lst[i], str):
            del lst[i]
        else:
            i += 1
    return lst

print(str_sorted([1, 10, 'pp', True, 'hello', 'a', 3, False, None, 'b']))