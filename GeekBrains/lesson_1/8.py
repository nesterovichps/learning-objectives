# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:

import math

print('formula ax² + bx + c = 0')
formula_a = int(input('enter a '))
formula_b = int(input('enter b '))
formula_c = int(input('enter c '))
print('You enter formuls {}x²+{}x+{}=0'.format(formula_a, formula_b, formula_c))

D = formula_b ** 2 - 4 * formula_a * formula_c

if D > 0:
    x1 = ((-formula_b) + math.sqrt(D)) / (2 * formula_a)
    x2 = ((-formula_b) - math.sqrt(D)) / (2 * formula_a)
    print('x1 = {}, x2 = {}'.format(x1, x2))
elif D == 0:
    x = (-formula_b) / (2*formula_a)
    print('x = {}'.format(x))
else:
    print('no roots')
