'''
Exercise: walking the loop

Objective. Trace through the execution of a while-loop by hand.
Here’s the code to find integer factors again:

number = 6

possible_factor = 1
while possible_factor <= number:
    if number % possible_factor == 0:
        print( str(possible_factor) + " is a factor of " + str(number) + "." )

    possible_factor = possible_factor + 1

print( "And that's all the factors of " + str(number) + "." )

Step through the code mentally, recording into the text box below the value of the program counter, the values of variables, the values of
interesting expressions, and output to the screen; some values have been entered to get you started.

1 number: 6
3 possible_factor: 1

4 (possible_factor <= number): true
5 (number % possible_factor): 0
  (number % possible_factor == 0): true
6 OUTPUT:  "1 is a factor of 6"
'''
