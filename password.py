"""
Программа оценивает сложность пароля.

Пользователь вводит пароль, в ответ получает оценку "сложный"/"простой"
Сложным считается пароль, состоящий как минимум из 8-ми символов,
включая цифры и алфавитные символы
"""


def password_evaluation():
    user_password = input('Введите пароль: ')
 
    password_requirements = {'digits': 0, 'capital letters': 0}
 
    if len(user_password) >= 8 and user_password.isalnum():
        for symbol in user_password:
            if symbol.isdigit():
                password_requirements['digits'] += 1
            elif symbol.isupper():
                password_requirements['capital letters'] += 1
 
        if password_requirements['digits'] < 1:
            print('Пароль простой. Рекомендуем добавить в пароль цифры.')        
        elif password_requirements['capital letters'] < 1:
            print('Пароль простой. Рекомендуем добавить в пароль буквы в верхнем регистре.')      
        else:
            print('Пароль сложный и отвечает всем требованиям безопасности.')
    else:
        print('Ваш пароль слишком простой. Он должен состоять, как минимум, из 8-ми алфавитных символов.')


if __name__ == '__main__':
    password_evaluation()
