from Beginner_Files.ReeborgsWorldLibraryMethods import *


def reach_goal():
    while at_goal() != True:
        while(front_is_clear() and at_goal() != True):
            move()
        if(wall_in_front()):
            jump()

reach_goal()

    
    

