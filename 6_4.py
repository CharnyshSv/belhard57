# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка
# незаконно
from typing import List

lst = [1, 10, 'pp', True, 'hello', 'a', 3, False, None]

def filter_terms(lst):
    lst = [i for i in lst if isinstance(i, str)]
    return lst

print(filter_terms(lst))

