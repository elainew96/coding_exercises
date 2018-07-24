'''
Exercise: 5 squares

Objective: write a while loop to cause repeated behavior.
Now write a program using a single while-loop that causes the robot to drive 4 squares in a row.
'''
from robotsim import left, forward, right, start_simulator
start_simulator()
square = 0
while (square<4):
    for _ in range(0,4): #draws one square
        forward(100)
        left(90)
    square += 1
