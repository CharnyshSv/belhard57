word1: str = "Hello"
word2: str = "Python"
print(word1, word2, sep="-")

text: str = input('Enter text') # Hello my dear friend
words: str = text.split(' ')
text: str = '-'.join(words)
print(text)
