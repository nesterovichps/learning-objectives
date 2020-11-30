#!/usr/bin/python3

from pyrob.api import *

def krest():
    move_down(2)
    move_right()
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
    move_left(2)
@task(delay=0.01)
def task_2_1():
    krest()
    move_down()
    move_right()


if __name__ == '__main__':
    run_tasks()
