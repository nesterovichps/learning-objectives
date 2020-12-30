# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import sys,os
import shutil
path_this=os.getcwd()
file_name=sys.argv[0].split('/')[-1]

shutil.copyfile(f'{path_this}/{file_name}',
                f'{path_this}/copy_{file_name}')