# #!/usr/bin/python3
#
# """
# == Лото ==
#
# Правила игры в лото.
#
# Игра ведется с помощью специальных карточек, на которых отмечены числа,
# и фишек (бочонков) с цифрами.
#
# Количество бочонков — 90 штук (с цифрами от 1 до 90).
#
# Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
# расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
#
# --------------------------
#     9 43 62          74 90
#  2    27    75 78    82
#    41 56 63     76      86
# --------------------------
#
# В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
# случайная карточка.
#
# Каждый ход выбирается один случайный бочонок и выводится на экран.
# Также выводятся карточка игрока и карточка компьютера.
#
# Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
# Если игрок выбрал "зачеркнуть":
# 	Если цифра есть на карточке - она зачеркивается и игра продолжается.
# 	Если цифры на карточке нет - игрок проигрывает и игра завершается.
# Если игрок выбрал "продолжить":
# 	Если цифра есть на карточке - игрок проигрывает и игра завершается.
# 	Если цифры на карточке нет - игра продолжается.
#
# Побеждает тот, кто первый закроет все числа на своей карточке.
#
# Пример одного хода:
#
# Новый бочонок: 70 (осталось 76)
# ------ Ваша карточка -----
#  6  7          49    57 58
#    14 26     -    78    85
# 23 33    38    48    71
# --------------------------
# -- Карточка компьютера ---
#  7 11     - 14    87
#       16 49    55 77    88
#    15 20     -       76  -
# --------------------------
# Зачеркнуть цифру? (y/n)
#
# Подсказка: каждый следующий случайный бочка из мешка удобно получать
# с помощью функции-генератора.
#
# Подсказка: для работы с псевдослучайными числами удобно использовать
# модуль random: http://docs.python.org/3/library/random.html
#
# """
import random
import time
import numpy as np


class Person:
    def __init__(self, name, list_cask):
        self.all_column = [list_cask[0:9], list_cask[9:19], list_cask[19:29],
                           list_cask[29:39], list_cask[39:49], list_cask[49:59],
                           list_cask[59:69], list_cask[69:79], list_cask[79:90]]
        self.name = name
        self.created_card()

    def created_card(self):
        line1 = ['===========================']
        if self.name == 'Player':
            line2 = ['------Карточка Игрока------']
        else:
            line2 = ['----Карточка Компьютера----']
        line3 = self.get_line()
        line4 = self.get_line()
        line5 = self.get_line()
        line6 = ['===========================']
        self.card = [line1, line2, line3, line4, line5, line6]

    def get_line(self):
        result_line = []
        line = list(np.random.choice(
            [random.choice(self.all_column[0]), random.choice(self.all_column[1]), random.choice(self.all_column[2]),
             random.choice(self.all_column[3]), random.choice(self.all_column[4]), random.choice(self.all_column[5]),
             random.choice(self.all_column[6]), random.choice(self.all_column[7]), random.choice(self.all_column[8])],
            size=5, replace=False))
        line.sort()
        index = 0
        for el in range(9):
            if line[index] in self.all_column.copy()[el]:
                result_line.append(line[index])
                self.all_column[el].remove(line[index])
                if index < 4:
                    index += 1
            else:
                result_line.append('  ')
        return result_line

    def check_card(self, choise_player,cask):
        print(f'{self.name} выбрал {choise_player}')
        if choise_player =='+':
            for j in range(2, 5):
                if str(cask) in str(self.card[j]):
                        return self.update_card(cask)
            return False,True
        else:
            #     choise_player=='-'
            for j in range(2, 5):
                if str(cask) in str(self.card[j]):
                        return False,True
            return False,False



    def show_card(self):

        print(*self.card[0])
        print(*self.card[1])
        print(*[str(number).rjust(2) for number in self.card[2]], sep=' ')
        print(*[str(number).rjust(2) for number in self.card[3]], sep=' ')
        print(*[str(number).rjust(2) for number in self.card[4]], sep=' ')
        print(*self.card[5])
        print()

    def update_card(self,cask):
        for j in range(2,5):
            for i in range(9):
                if self.card[j][i]==cask:
                    self.card[j][i]='-'
        if str(self.card[2]).count('-')+str(self.card[3]).count('-')+str(self.card[4]).count('-')==15:
                    return True,False
        return False,False

class Game:
    def __init__(self):
        self.list_cask = [cask for cask in range(1, 91)]
        self.cask_in_bag = 90
        self.player = Person('Player', self.list_cask)
        self.enemy = Person('Enemy', self.list_cask)
        self.start_game()

    def start_game(self):
        print('Карточка Игрока создана')
        self.player.show_card()
        print('Карточка Компьютера создана')
        self.enemy.show_card()
        time.sleep(0.5)
        win_player=False
        win_computer=False
        faile_player=False
        faile_computer=False
        while self.list_cask:
            cask_now=self.get_cask()
            win_player,faile_player=self.player_move(cask_now)
            if faile_player ==True:
                win_computer=True
            else:
                win_computer,faile_computer=self.computer_move(cask_now)
            if faile_computer==True:
                win_player=True
            self.player.show_card()
            self.enemy.show_card()
            if win_player or win_computer:
                break
        print('==================')
        print('    Итог игры')
        self.check_win(win_player,win_computer)
        print('==================')
        print()
        self.player.show_card()
        self.enemy.show_card()

    def get_cask(self):

        cask=random.choice(self.list_cask)
        self.list_cask.remove(cask)
        print(f'Выпало число {cask} в мешке осталось {len(self.list_cask)} боченков')
        return cask


    def player_move(self,cask):
        choise_player=input('Введите "+" если число есть на карточке, "-" если нет: ')
        while choise_player!='+' and choise_player!='-':
            print('Вы ввели неверное значение')
            choise_player=input('Введите "+" если число есть на карточке, "-" если нет: ')
        # ---AUTO GAME---
        # choise_player = '-'
        # for j in range(2, 5):
        #     if str(cask) in str(self.player.card[j]):
        #             choise_player = '+'

        return (self.player.check_card(choise_player,cask))

    def computer_move(self,cask):
        choise_player='-'
        for j in range(2, 5):
            if str(cask) in str(self.enemy.card[j]):
                choise_player = '+'
        return (self.enemy.check_card(choise_player,cask))
    def check_win(self,win_player,win_computer):
        if win_player and win_computer:
            print('Боевая ничья')
        elif win_player:
            print('Выиграл Игрок')
        elif win_computer:
            print('Выиграл Компьютер')
        else:
            print('ERROR WIN ')

game = Game()
