# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
import random

int_list = [random.randint(-100, 101) for _ in range(30)]
print(*int_list)
result_list = [i ** 2 for i in int_list]
print(*result_list)
