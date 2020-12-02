# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]
def square(list_integer):
    for element in list_integer:
        if element ** 0.5 and element >= 0:
            square = element ** 0.5
            if square == int(square):
                result_list.append(int(square))
    print(result_list)


result_list = list()
list_integer = [-5, -6, 0, 1, 1, 2, 2, 3, 4, 5, 5, 6, 6, 7, 8, 9, 1, 1, 10, 10, 3, 3, 11, 20, 5, 12, 7, 13, 9, 14]
controlling_list = [2, -5, 8, 9, -25, 25, 4]

square(controlling_list)
square(list_integer)
