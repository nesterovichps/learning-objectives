# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))


ABC = []
with open('data/fruits.txt', 'r', encoding='UTF-8') as file:
    for frout in file.readlines():
        frout = frout.strip()
        if frout:
            print(frout.strip())
            char = frout[0].upper()
            if char in ABC:
                with open(f'data/fruits_list/fruits_{char}.txt', 'a', encoding='UTF-8') as file_add:
                    file_add.write(frout + '\n')
            else:
                with open(f'data/fruits_list/fruits_{char}.txt', 'w', encoding='UTF-8') as file_add:
                    file_add.write(frout + '\n')
                    ABC.append(char)
