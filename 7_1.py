# Дано натуральное число N. Выведите слово YES,
# если число N является точной степенью двойки, или слово NO в противном случае.
# Без использования оператора возведения в степень. Сделать с помощью рекурсии

def is_step_two(N: int) -> bool:
    if N != 1:
        if not N % 2:
            return is_step_two(N // 2)
        return False
    else:
        return True

print(is_step_two())