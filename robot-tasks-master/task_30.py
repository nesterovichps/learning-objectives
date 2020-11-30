#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    x=0
    while not wall_is_on_the_right():
        move_right()
        x+=1
    a=x-1
    # print(a)
    while a>0:
        for i in range(a):
            move_left()
            fill_cell()
        move_down()
        if a>1:
            move_right(a-1)
        a=a-2
    a=x-1
    # print(111)
    while not wall_is_above():
        move_up()
    while not wall_is_on_the_left():
        move_left()
    while a > 0:
        for i in range(a):
            move_down()
            fill_cell()
        move_right()
        if a > 1:
            move_up(a - 1)
        a = a - 2
    a = x - 1
    while not wall_is_beneath():
        move_down()
    while not wall_is_on_the_left():
        move_left()
    while a > 0:
        for i in range(a):
            move_right()
            fill_cell()
        move_up()
        if a > 1:
            move_left(a - 1)
        a = a - 2
    a = x - 1
    while not wall_is_beneath():
        move_down()
    while not wall_is_on_the_right():
        move_right()
    while a > 0:
        for i in range(a):
            move_up()
            fill_cell()
        move_left()
        if a > 1:
            move_down(a - 1)
        a = a - 2
    while not wall_is_beneath():
        move_down()
    while not wall_is_on_the_left():
        move_left()






if __name__ == '__main__':
    run_tasks()
