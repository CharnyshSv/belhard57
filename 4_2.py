# Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры
text: str = input('Enter text')  # вести текст
dictionary = {symbol: text.count(symbol) for symbol in text}
print(dictionary)