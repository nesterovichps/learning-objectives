#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
    y = 0
    while not wall_is_on_the_right():
        move_right()
        if wall_is_beneath() and not wall_is_above():
            move_up()
            x = 1
            while not wall_is_above():
                fill_cell()
                move_up()
                x += 1

            # print(1)
            # move_up()
            else:
                fill_cell()
            # move_down(x)
            move_down(x)

        y += 1
    move_left(y)


if __name__ == '__main__':
    run_tasks()
