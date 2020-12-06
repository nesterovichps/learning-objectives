#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_1_2():
    move_right(2)
    move_down(2)
    fill_cell()
    move_right(2)
    move_down()
    # fill_cell()


if __name__ == '__main__':
    run_tasks()
