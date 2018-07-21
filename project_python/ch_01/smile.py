'''
Exercise: smile

Objective: learn how to call drawing library functions that take parameters, in order to draw a desired complex picture.
Write a program that causes a yellow smiley face to be drawn on the screen. You have a 200 by 200 window available.
Draw the outline of the face. Put your code for drawing the outline after the line # draw the outline of the face. (Lines that begin with # are ignored by the computer, and are for human readers only.
Draw the eyes. Put your code for drawing the eyes after the line # draw the eyes.
Bonus challenge. Draw the mouth. Hint – draw a circle, and then erase the top part of it by drawing some sort of yellow shape.
'''
from cs1lib import start_graphics, clear, draw_circle, draw_rectangle, set_fill_color, set_stroke_color

def draw():

    # draw a white background
    clear()

    # draw the outline of the face
    set_fill_color(1, 1, 0)
    draw_circle(100,75,50)   
    
    # draw the mouth
    draw_circle(100,80,30)
    set_stroke_color(1,1,0)
    draw_rectangle(62,45,75,45)
    
    # draw the eyes
    set_fill_color(0,0,0)
    set_stroke_color(0,0,0)
    draw_circle(75,60,5)
    draw_circle(125,60,5)

start_graphics(draw)
