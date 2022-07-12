# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка
# незаконно
from typing import List

lst: list[int | str | bool | None] = [1, 10, 'pp', True, 'hello', 'a', 3, False, None]

def filter_terms(lst):

    for i in lst:
        if isinstance(i, str):
            lst.append(i)
        else:
            lst.remove(i)
print(filter_terms(lst))

