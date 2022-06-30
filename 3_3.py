name: str = 'Alherd'
age: int = 10
town: str = 'Minsk'
text = f"My name is {name}. I'm {age} years old. I am from {town}."
print(text)

name: str = 'Alherd'
age: int = 10
town: str = 'Minsk'
text = 'My name is {name}. I\'m {age} years old. I\'m from {town}.'.format(name=name, age=age, town=town)
print(text)