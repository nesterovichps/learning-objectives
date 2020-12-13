# Задание-3 (Ферзи):
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били
# друг друга. Вам дана расстановка 8 ферзей на доске.
# Определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 — координаты 8 ферзей.
# Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.


def check(array, x, y):
    if array[x][y] != 5:
        array[x][y] = 1
    else:
        array[x][y] = 9
        print('YES', x, y)
        print(*array, sep='\n')
        exit()


def trajectory(array, y, x):
    if array[x][y] == 0:
        array[x][y] = 5
        for vertical in range(8):
            if array[vertical][y] == array[x][y]:
                continue
            check(array, vertical, y)

        for horizontal in range(8):
            if array[x][horizontal] == array[x][y]:
                continue
            check(array, x, horizontal)

            # diagonal_l_r
            i = 1
        while x - i >= 0 and y - i >= 0:
            check(array, x - i, y - i)
            i += 1
        i = 1
        while x + i < 8 and y + i < 8:
            check(array, x + i, y + i)
            i += 1

        # diagonal_r_l
        i = 1
        while x - i >= 0 and y + i < 8:
            check(array, x - i, y + i)
            i += 1
        i = 1
        while x + i < 8 and y - i >= 0:
            check(array, x + i, y - i)
            i += 1
    else:
        array[x][y] = 9
        print('YES', x, y)
        print(*array, sep='\n')
        exit()
    return array


ferz = (1, 4), (2, 2), (3, 7), (4, 3), (5, 6), (6, 8), (7, 5), (8, 1)  # GOOD
# ferz = (1, 4), (2, 2), (3, 7), (4, 3), (5, 6), (6, 8), (7, 5), (8, 1) # GOOD
# ferz = (1, 5), (2, 2), (3, 4), (4, 7), (5, 3), (6, 8), (7, 6), (8, 1) # GOOD
# ferz = (1, 3), (2, 5), (3, 2), (4, 8), (5, 6), (6, 4), (7, 7), (8, 1) # GOOD
# ferz = (7, 8), (2, 2), (8, 5), (4, 3), (5, 7), (1, 4), (6, 1), (3, 6) # BAD
array = [[0] * 8 for i in range(8)]
for f in ferz:
    array = trajectory(array, f[0] - 1, f[1] - 1)

print('NO')
print(*array, sep='\n')
