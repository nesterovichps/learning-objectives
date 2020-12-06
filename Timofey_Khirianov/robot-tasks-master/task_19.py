#!/usr/bin/python3

from pyrob.api import *


def check():
    if not wall_is_above():
        # print ('good')
        return True


@task(delay=0.01)
def task_8_29():
    while not wall_is_on_the_left():
        move_left()
        i = check()
        if i:
            while not wall_is_above():
                move_up()
            while not wall_is_on_the_left():
                move_left()
            break
    while not wall_is_on_the_right() and not i:
        move_right()
        i = check()
        if i:
            while not wall_is_above():
                move_up()
            while not wall_is_on_the_left():
                move_left()
            break


if __name__ == '__main__':
    run_tasks()
