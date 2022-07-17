# Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int

#number = int(input('Число в десятичной СС: '))
#numberb = ''
# while number > 0:
#    numberb = str(number % 2) + numberb
#    number = number // 2
#print(numberb)
#print(bin(2))


def decimal_to_bin_converter(decimal: int) -> str:
    result: str = ""
    while decimal:
        result += str(decimal % 2)
        decimal //= 2
    return result[::-1]

#print(bin(17))
#print(decimal_to_bin_converter(17))

def bin_to_decimal_converter(bin_number: str) -> int:
    decimal: int = 0
    for i in bin_number:
        decimal = decimal * 2 + int(i)
    return decimal

print(bin_to_decimal_converter("10001"))