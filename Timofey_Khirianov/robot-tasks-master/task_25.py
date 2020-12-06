#!/usr/bin/python3

from pyrob.api import *


def krest():
    move_down(2)

    fill_cell()
    move_down()
    move_right()
    fill_cell()
    move_right()
    move_up()
    fill_cell()
    move_left()
    fill_cell()
    move_up()
    fill_cell()
    move_up()
    move_left()


@task(delay=0.01)
def task_2_2():
    for i in range(5):
        krest()
        if i < 4:
            move_right(4)
    move_down()


if __name__ == '__main__':
    run_tasks()
