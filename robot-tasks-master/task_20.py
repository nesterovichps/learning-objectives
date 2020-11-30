#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_4_3():
    move_right()
    n=27
    for i in range(12):
        for j in range(n):
            fill_cell()
            move_right()
        move_down()
        move_left(n)


if __name__ == '__main__':
    run_tasks()
