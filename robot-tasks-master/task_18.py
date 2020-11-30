#!/usr/bin/python3

from pyrob.api import *
def check(i):
    if not wall_is_above():
        i+=1
    if not wall_is_beneath():
        i+=1
    if not wall_is_on_the_left():
        i+=1
    if not wall_is_on_the_right():
        i+=1
    return i

@task(delay=0.01)
def task_8_28():
    while not wall_is_on_the_left():
        move_left()

    while not wall_is_on_the_right():
        i = 0
        i = check(i)
        if wall_is_on_the_left() and i==2:
            x = True
            break
        if i == 3:
            x = True
            break
        move_right()
    while not wall_is_above():
        move_up()
    while not wall_is_on_the_left():
        move_left()




if __name__ == '__main__':
    run_tasks()
