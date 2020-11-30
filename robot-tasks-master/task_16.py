#!/usr/bin/python3

from pyrob.api import *
def check():
    if wall_is_above():
        while not wall_is_beneath():
            move_down()
    else:
        while not wall_is_above():
            move_up()

    if wall_is_on_the_left():
        while not wall_is_on_the_right():
            move_right()
    else:
        while not wall_is_on_the_left():
            move_left()

@task(delay=0.01)
def task_8_22():
    i=0
    while i!=3:
        i=0
        check()
        if wall_is_above():
            i+=1
        if wall_is_beneath():
            i+=1
        if wall_is_on_the_left():
            i+=1
        if wall_is_on_the_right():
            i+=1



if __name__ == '__main__':
    run_tasks()
