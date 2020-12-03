# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3
import math


def main(n):
    verge = 1
    numbers_below = 0
    while n > verge ** 2 + numbers_below:
        numbers_below += verge ** 2
        verge += 1
    temp_find_number = n - numbers_below

    result_left = temp_find_number % verge
    result_right = math.ceil(temp_find_number / verge)
    for i in range(1, verge):
        result_right += i

    if not result_left:
        result_left = verge

    print('вверх {} влево {}'.format(result_right, result_left))


if __name__ == '__main__':
    n = range(1, 1000)
    main(int(input('На какой этаж хотите поднятся ???')))

    print('{} {} {} {} {} {}'.format(n[85], n[86], n[87], n[88], n[89], n[90]).center(17))
    print('{} {} {} {} {} {}'.format(n[79], n[80], n[81], n[82], n[83], n[84]).center(17))
    print('{} {} {} {} {} {}'.format(n[73], n[74], n[75], n[76], n[77], n[78]).center(17))
    print('{} {} {} {} {} {}'.format(n[67], n[68], n[69], n[70], n[71], n[72]).center(17))
    print('{} {} {} {} {} {}'.format(n[61], n[62], n[63], n[64], n[65], n[66]).center(17))
    print('{} {} {} {} {} {}'.format(n[55], n[56], n[57], n[58], n[59], n[60]).center(17))
    print('{} {} {} {} {}'.format(n[50], n[51], n[52], n[53], n[54]).center(17))
    print('{} {} {} {} {}'.format(n[45], n[46], n[47], n[48], n[49]).center(17))
    print('{} {} {} {} {}'.format(n[40], n[41], n[42], n[43], n[44]).center(17))
    print('{} {} {} {} {}'.format(n[35], n[36], n[37], n[38], n[39]).center(17))
    print('{} {} {} {} {}'.format(n[30], n[31], n[32], n[33], n[34]).center(17))
    print('{} {} {} {}'.format(n[26], n[27], n[28], n[29]).center(17))
    print('{} {} {} {}'.format(n[22], n[23], n[24], n[25]).center(17))
    print('{} {} {} {}'.format(n[18], n[19], n[20], n[21]).center(17))
    print('{} {} {} {}'.format(n[14], n[15], n[16], n[17]).center(17))
    print('{} {} {}'.format(n[11], n[12], n[13]).center(17))
    print('{} {} {}'.format(n[8], n[9], n[10]).center(17))
    print('{} {} {}'.format(n[5], n[6], n[7]).center(17))
    print('{} {}'.format(n[3], n[4]).center(17))
    print('{} {}'.format(n[1], n[2]).center(17))
    print('{}'.format(n[0]).center(17))
