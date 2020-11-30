#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_4_11():
    x = 1
    move_right()
    n = 13
    h = 1
    for i in range(14):
        for j in range(n):
            if h < x:
                fill_cell()
                h += 1
            move_right()
        move_down()
        move_left(n)
        x += 1
        h = 1


if __name__ == '__main__':
    run_tasks()
