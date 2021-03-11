# -*- coding: utf-8 -*-

from random import randint


# Создаем случайное 4-х значное число(не начинается на ноль, все цифры разные)
def number_creation():
    global number
    number = []
    while len(number) < 4:
        rand_digit = randint(0, 9)
        if rand_digit in number:  # если цифра есть в числе, запускаем заново
            continue
        number.append(rand_digit)
        if number[0] == 0:  # если первый элемент списка 0, то запускаем генерацию числа заново
            number = []
    return number


# проверка числа на соответствие нашим параметрам:
#     - 4-х значное число
#     - цифры не повторяются
#     - число не начинается на ноль
def number_check(user_number):
    if not user_number.isdigit():
        return 'Ошибка, можно вводить только цифры'
    elif len(user_number) != 4:
        return 'Ошибка, число должно быть 4-х значным'
    elif user_number[0] == '0':
        return 'Ошибка, число не должно начинаться на 0 (ноль)'
    elif len(set(user_number)) < 4:
        return 'Ошибка, цифры в числе не должны повторяться'


# подсчет результатов
def calculation_of_result(user_number):
    bulls = 0
    cows = 0
    for i, digit in enumerate(user_number):
        if int(digit) == number[i]:  # если цифра на той же позиции, что и в загаданном числе
            bulls += 1
        if int(digit) in number:  # если цифра есть в загаданном числе
            cows += 1

    # Добавление результата в статистику по игре
    results.append(f'{user_number} - Быков: {bulls}, Коров: {cows - bulls}')

    # Результат текущего хода
    return {'Быков': bulls, 'Коров': cows - bulls}


def game_results():
    return results


def game_over():
    while True:
        user_choice = input('Желаете сыграть еще? (да/нет) ')
        if user_choice.upper() in ['Y', 'YES', 'ДА']:
            global results
            results = []  # сбрасываем старый результат
            return True
        elif user_choice.upper() in ['N', 'NO', 'НЕТ']:
            return False
        else:
            print('Введите да или нет')
            continue


number = []
results = []
