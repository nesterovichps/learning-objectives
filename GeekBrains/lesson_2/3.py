# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

list_integer = [-5, -6, 0, 1, 1, 2, 2, 3, 4, 5, 5, 6, 6, 7, 8, 9, 1, 1, 10, 10, 3, 3, 11, 20, 5, 12, 7, 13, 9, 14]
result_list = list()
for element in list_integer:
    if element % 2 == 0:
        result_list.append(element / 4)
    else:
        result_list.append(element * 2)
print(*result_list)
