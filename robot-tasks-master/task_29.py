#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_7_7():
    x = 3
    y = 0
    while not wall_is_on_the_right():

        move_right()
        if cell_is_filled():
            y=0
            y += 1
            if not wall_is_on_the_right():
                move_right()

            if cell_is_filled() :
                y += 1
                if  not wall_is_on_the_right():
                    move_right()
                if cell_is_filled():
                    y += 1

                else:
                    y = 0
            else:
                y=0
        if x == y:
            break


if __name__ == '__main__':
    run_tasks()
