# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;

variable_one, variable_two = input('Input integer №1 \n'), input('Input integer №2 \n')
variable_one, variable_two = variable_two, variable_one
print(f'Integer №1 = {variable_one} Integer №2 = {variable_two}')
