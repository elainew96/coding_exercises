'''
Exercise: square dance

Objective: Build complex behavior from a repeating sequence of simple behaviors.
Add only forwards and left function calls to cause the robot to move in a square:
'''
from robotsim import left, forward, right, start_simulator
start_simulator()

forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)

'''
for _ in range(0,4):
    forward(100)
    left(90)
'''
