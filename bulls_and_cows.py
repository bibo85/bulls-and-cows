# -*- coding: utf-8 -*-

from bulls_and_cows_engine import number_creation, number_check, calculation_of_result, game_results, game_over
from termcolor import cprint


# Игра «Быки и коровы»
# https://goo.gl/Go2mb9
#
# Правила:
# Компьютер загадывает четырехзначное число, все цифры которого различны
# (первая цифра числа отлична от нуля). Игроку необходимо разгадать задуманное число.
# Игрок вводит четырехзначное число c неповторяющимися цифрами,
# компьютер сообщают о количестве «быков» и «коров» в названном числе
# «бык» — цифра есть в записи задуманного числа и стоит в той же позиции,
#       что и в задуманном числе
# «корова» — цифра есть в записи задуманного числа, но не стоит в той же позиции,
#       что и в задуманном числе
#
# Например, если задумано число 3275 и названо число 1234,
# получаем в названном числе одного «быка» и одну «корову».
# Очевидно, что число отгадано в том случае, если имеем 4 «быка».

def game():
    while True:
        user_number = input('Введите целое 4х значное число: ')

        # Если с проверки что-то пришло, значит есть ошибка
        result_check = number_check(user_number)
        if result_check:
            cprint(result_check, color='red')
            continue

        # обработка и вывод информации по введенному числу
        result = calculation_of_result(user_number)
        cprint(result, color='yellow')

        # Вывоз статистики по текущей игре
        cprint('Попытки:', color='blue')
        for i, text in enumerate(game_results()):
            i += 1
            cprint(f'{i}. {text}', color='blue', end='\n')

        # Число угадано, выходим из функции
        if result['Быков'] == 4:
            cprint('Поздравляем, Вы угадали число!', color='green')
            return True


while True:
    number_creation()  # создаем число
    # print(number_creation())
    cprint('Загадано 4х значное число. Попробуйте отгадать.', color='cyan')

    # Заходим в игру
    number_guessed = game()  # Число угадано -> True

    # Если число угадано, то делаем заход на новую игру
    if number_guessed:
        new_game = game_over()
        if new_game:
            continue
        else:
            print('Игра окончена')
            break
