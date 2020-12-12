# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.
import random

with open('2500_random_integer.txt', 'w', encoding='UTF-8') as _:
    pass
with open('2500_random_integer.txt', 'a', encoding='UTF-8') as f:
    for i in range(2500):
        f.write(str(random.randint(0, 9)))
result_list = []
colculate = 0
with open('2500_random_integer.txt', 'r', encoding='UTF-8') as f:
    sourse = f.read()
    print(sourse)
    for i in range(10):
        result_list.append([i, 0])
        for number in sourse:
            if int(number) == int(result_list[i][0]):
                colculate += 1
            else:
                if int(result_list[i][1]) < colculate:
                    result_list[i][1] = colculate
                colculate = 0
        colculate = 0
max_number = 0
max_number_round = 0
for item, values in result_list:
    if values > max_number_round:
        max_number, max_number_round = item, values

print(result_list)
print(max_number, max_number_round)
