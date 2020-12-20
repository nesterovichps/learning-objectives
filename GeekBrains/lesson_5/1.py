# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
def add_dir():
    for i in range(1,10):
        os.mkdir(f'dir_{i}')
def del_dir():
    for i in range(1,10):
        os.rmdir(f'dir_{i}')
# add_dir()
# del_dir()