# Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
# пустая строка)
users = {
    1: {
        'fname': 'Alex',
        'lname': 'Pupkin',
        'telnumb': '375291111111',
        'email': 'alex@test.com'
    },
    2: {
        'fname': 'ALena',
        'lname': 'Pupkina',
        'telnumb': '375293333333',
        'email': ''
    },
    3: {
        'fname': 'Yan',
        'lname': 'Pupkin',
        'telnumb': '375291111111'
    }
}

def get_users(users):
    for user in users.values():
        if 'email' not in user or not user['email']:
            return user['fname'], user['lname']

print(get_users(users))



