# https://bit.ly/3lXT30f

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    step = 0
    while not right_is_clear():
        move()
        step += 1
    turn_right()
    move()
    turn_right()
    for st in range(step):
        move()
    turn_left()

while not at_goal():
    if not wall_in_front():
        move()
    else:
        jump()