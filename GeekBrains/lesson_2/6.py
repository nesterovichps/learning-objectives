# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
import random
n=100
result_list=[]
for _ in range(n):
    result_list.append(random.randint(-10,10))
print(*result_list)