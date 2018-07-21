'''
Exercise: big smile

Objective: Use variables to allow behavior of code to be changed easily.
The code below will draw a smiley face on the screen, and you can use the variables x and y to change where the smiley face is drawn. But the smiley face is always the same size. Add a new variable, scale, that allows you to change the size of the smiley face to make the face either larger or smaller. For example, if scale had the value 2, then the code would draw the smiley face twice as large (but still centered on x and y).
Test your code by changing variable values a few times to draw the smiley face at different locations at both small and large scale
'''
from cs1lib import start_graphics, clear, draw_circle, draw_rectangle, set_fill_color, set_stroke_color

def draw():
    
    scale = 1
    x = 100
    y = 100

    # draw a white background
    clear()

    # draw the outline of the face
    set_fill_color(1, 1, 0)   # set fill color to yellow
    draw_circle(x, y, 50*scale)

    # draw the mouth
    set_fill_color(1, 1, 0)  # yellow
    draw_circle(x, y, 30*scale)
    set_stroke_color(1, 1, 0)
    draw_rectangle((x - 32*scale), (y - 32*scale), 62*scale, 40*scale)

    # draw the eyes
    set_stroke_color(0, 0, 0)
    set_fill_color(0, 0, 0)  # set fill color to black
    draw_circle((x - 20*scale), (y - 10*scale), 5*scale)
    draw_circle((x + 20*scale), (y - 10*scale), 5*scale)

start_graphics(draw)
