#!/usr/bin/python3

from pyrob.api import *


def check():
    while not wall_is_on_the_right():
        move_right()
    while wall_is_beneath():
        if wall_is_on_the_left():
            return
        move_left()

    else:
        # if wall_is_beneath():
        #     return
        move_down()


@task(delay=0.01)
def task_8_30():
    while not wall_is_on_the_left():
        check()


if __name__ == '__main__':
    run_tasks()
