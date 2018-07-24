'''
Exercise: optimize factors

Objective. Modify existing code to implement a more efficient algorithm.
The code for computing factors is inefficient. It loops from 1 to the number, but I claim it should only loop from 1 to the square root of
the number, since factors come in pairs. For example, if 2 is a factor of 42, then so is 21. Re-write the following code so that it 
iterates fewer times through the loop, but still prints out all of the factors. Don’t forget to import the sqrt function from the math 
module.
'''
from math import sqrt

number = 42

possible_factor = 1
while possible_factor <= sqrt(number):
    if number % possible_factor == 0:
        print( str(possible_factor) + " is a factor of " + str(number) + "." )
        print( str(number/possible_factor) + " is a factor of " + str(number) + "." )

    possible_factor = possible_factor + 1

print( "And that's all the factors of " + str(number) + "." )
