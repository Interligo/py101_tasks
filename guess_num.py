"""
Программа генерирует число от 0 до 1_000_000 и предлагает угадать его.

Программа должна приветствовать пользователя и считывать число с клавиатуры
Если число меньше загаданного, то программа выводит сообщение о том, что число
меньше
Если больше загаданного, то программа выводит сообщение о том, что больше

Программа должна выводить сообщения-предупреждения, если:
* пользователь ввёл не число
* число не входит в обозначенный в условии диапазон
Если пользователь ничего не ввёл/ввёл "exit", то происходит выход из программы.

Тебе может понадобится модуль random, цикл while и ветвления
"""


def guess_digit(): 
    number = random.randint(0, 1000000)
    try_counter = 0

    print('Привет!')
    print('Число загадано. Попробуйте его отгадать.')    
 
    while True:
        answer = input('Введите число: ')
    
        if answer == '' or answer == 'exit':
            print('Завершаю работу программы.')
            break
 
        if not answer.isdigit():
            print('Пожалуйста, введите положительное число.')
            continue
    
        if int(answer) > 1000000:
            print('Пожалуйста, введите число в диапозоне от 0 до 1 000 000.')
            continue
 
        answer = int(answer)
        try_counter += 1
 
        if answer == number:
            print(f'Верно! Вы отгадали число {number} за cледующее количество попыток - {try_counter}.')
            break 
        elif answer < number:
            print('Загаданное число больше.')
        else:
            print('Загаданное число меньше.')


if __name__ == '__main__':
    import random

    guess_digit() 
