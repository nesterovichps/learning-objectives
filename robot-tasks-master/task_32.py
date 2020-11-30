#!/usr/bin/python3

from pyrob.api import *


def chexk():
    x=0
    if wall_is_above() and wall_is_beneath():
        if cell_is_filled():
            x+=1
        else:
            fill_cell()
        return x
    if wall_is_beneath() and not wall_is_above():
        while not wall_is_above():
            move_up()
            if cell_is_filled():
                x += 1
            else:
                fill_cell()
        while not wall_is_beneath():
            move_down()
        return x


@task(delay=0.01)
def task_8_18():
    v=0

    while not wall_is_on_the_right():
        v+=chexk()
        move_right()
    # print(v)
    mov('ax', v)


if __name__ == '__main__':
    run_tasks()
