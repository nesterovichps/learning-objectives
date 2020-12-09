
# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random

int_list = [random.randint(-100, 101) for _ in range(30)]
print(*int_list)
result_list=[el for el in int_list if el%3==0 and el>0 and el%4!=0]
print(result_list)