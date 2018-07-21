'''
Exercise: hello, hello!
Objective: Write and call your own functions to learn how the program counter steps through code.

You will write a program that introduces you and prints your favorite number.

Write the body of the function print_favorite_number
Write a function call at the end of the program that calls print_favorite_number.
Write a new function, say_introduction that prints Hello, my name is X. and I am a Y. on two separate lines, where X and Y are replaced by whatever you like.
Add a line that calls say_introduction so that the introduction is printed before the favorite number.
'''

def print_favorite_number():
    print("My favorite number is 6!")

def say_introduction():
    print("Hello, my name is Elaine.")
    print("I am a UC Davis alumni.")

say_introduction()
print_favorite_number()
