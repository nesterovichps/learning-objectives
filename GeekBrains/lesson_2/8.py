# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.
import matplotlib.pyplot as plt
import numpy as np

task = input("Введите график функции вида y = kx + b. Пример 2x-27 \n")
k, b = map(int, task.split('x'))
x = int(input("Введите х координату"))
y = k * x + b
print(f'Координате х = {x} соответствует У координата, равная {y}')
fig = plt.subplots()
x = np.linspace(x - 10, x + 10, 100)
y = lambda x: k * x + b
plt.plot(x, y(x))
plt.show()
