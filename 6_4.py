# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка
# незаконно
lst=[1, 10, 'pp', True, 'hello', 'a', 3, False, None]

def filter_terms(lst):
    lst = []
    for i in lst:
        if isinstance(i, str):
            lst.append(i)
            return lst

print(filter_terms(lst))