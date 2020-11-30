#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_7_5():
    x = 0
    y = 0
    while not wall_is_on_the_right():

        move_right()
        if x == y:
            if not wall_is_on_the_right():
                fill_cell()
            y = 0
            x += 1
        y += 1


if __name__ == '__main__':
    run_tasks()
