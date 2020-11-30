#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_7_6():
    x = 5
    y = 0
    while not wall_is_on_the_right():

        move_right()
        if cell_is_filled():
            y+=1
        if x == y:

            break




if __name__ == '__main__':
    run_tasks()
