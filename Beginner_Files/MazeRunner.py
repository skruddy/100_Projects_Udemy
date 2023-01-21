from Beginner_Files.ReeborgsWorldLibraryMethods import *


def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while not right_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

def make_a_u_turn():
    turn_left()
    turn_left()

def reach_goal():
    while at_goal() != True:
        if right_is_clear():
            turn_right()
            move()
        elif front_is_clear():
            move()
        else:
            turn_left()

while front_is_clear():
    move()
reach_goal()




