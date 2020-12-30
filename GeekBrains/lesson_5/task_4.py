# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

import os
import shutil
import sys

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл (запросить подтверждение операции)")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")


def make_dir():

    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")


def cp():
    # <file_name> - создает копию указанного файла
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    path_this = os.getcwd()
    file_name = dir_name
    try:
        shutil.copyfile(f'{path_this}/{file_name}',
                        f'{path_this}/copy_{file_name}')
        print('копия файла {} создана'.format(file_name))
    except FileNotFoundError:
        print('копия не создана {} исходного файла не существует'.format(file_name))


def rm():
    #   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    path_this = os.getcwd()
    file_name = dir_name

    if file_name in os.listdir():
        while True:
            print(f'Вы точно хотите удалить файл {file_name} ? Введите "да" для подтверждения "нет" для отмены')
            confirm = input()
            if confirm == "да":

                try:
                    os.remove(f'{path_this}/{file_name}')
                    print(f'Файл {file_name} удален')
                    return
                except FileNotFoundError:
                    print(' Не удается найти указанный файл')
            elif confirm == "нет":
                print('Операция отменена, файл не удален')
                return
    else:
        print(' Не удается найти указанный файл')


def cd():
    #   cd <full_path or relative_path> - меняет текущую директорию на указанную
    if not dir_name:
        print("Необходимо указать путь")
        return
    path_this = os.getcwd()
    new_directory = dir_name
    os.chdir(f'{new_directory}')
    print(os.getcwd())


def ls():
    #   ls - отображение полного пути текущей директории
    print(os.getcwd())


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": cp,
    "rm": rm,
    "cd": cd,
    "ls": ls
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
