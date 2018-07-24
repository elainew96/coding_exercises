'''
Exercise: even in a range

Objective: Write a boolean expression to test if a variable satisfies several conditions.
Write a single line of code that tests if the value of the variable x is even and has a value in the range 24 and 32 (inclusive), and prints out True if so, and False otherwise. Test your code with the values 0, 3, 24, 25, 32, 33, and 34.
'''
x = 24
print((x%2==0) and (x<=32) and (x>=24))
