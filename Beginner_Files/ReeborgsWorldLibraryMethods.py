def move():
    print("move")

def turn_left():
    print("turn_left")

def at_goal():
    pass

def front_is_clear():
    pass

def wall_in_front():
    pass

def right_is_clear():
    pass

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

