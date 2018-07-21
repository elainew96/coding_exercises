'''
Exercise: square function
Objective: Use a function to isolate a sequence of instructions, encapsulating a complex behavior. This is an example of abstraction.

Write a function single_square() that causes the robot to do a single square. Also write a while loop that calls single_square() 5 times, 
to cause the robot to drive in 5 squares.
'''
from robotsim import left, forward, right, start_simulator
start_simulator()

def single_square():
    for _ in range(0,4):
        forward(100)
        left(90)

square = 0
while (square<5):
    single_square()
    square += 1
