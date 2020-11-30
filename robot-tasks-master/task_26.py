#!/usr/bin/python3

from pyrob.api import *
def krest():
    move_down()

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
    move_left()


@task(delay=0.01)
def task_2_4():
    for i in range(5):
        for j in range(10):
            krest()
            if j < 9:
                move_right(4)
        move_left(36)
        if i <4:
            move_down(4)

    # move_down()


if __name__ == '__main__':
    run_tasks()
