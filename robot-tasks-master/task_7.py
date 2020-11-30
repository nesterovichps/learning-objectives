#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_5_4():
    iii = 0
    while not wall_is_beneath():
        move_down()
    while wall_is_beneath():
        iii+=1
        move_right()
    move_down()
    for i in range(iii):
        move_left()

if __name__ == '__main__':
    run_tasks()
