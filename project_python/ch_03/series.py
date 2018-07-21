'''
Exercise: series

Objective: Use multiple variables in a while loop to change loop body behavior on each iteration.
Write a program using a loop that prints first 100 numbers in the series of numbers: 1, 2, 4, 7, 11, 16, 22. Hint: The difference between
the two consecutive numbers increases by one for each new number. You may need a variable to keep track of the current rate of increase.
'''
counter = 0
num = 1
while (counter<100):
    print(num)
    counter += 1
    num += counter
