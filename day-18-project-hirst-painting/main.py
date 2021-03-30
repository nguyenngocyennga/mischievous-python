import random
import colorgram
from turtle import Turtle
from turtle import Screen
import turtle as turtle

image_colors = colorgram.extract('wave.jpg', 30)

pen_colors = []

for i in image_colors:
    new_rgb = i.rgb
    red = new_rgb[0]
    green = new_rgb[1]
    blue = new_rgb[2]
    new_pen_color = (red, green, blue)
    pen_colors.append(new_pen_color)
#
# print(pen_colors)

# set object color mode to recognize rgb tuples
turtle.colormode(255)
# pen_colors = [(245, 243, 238), (247, 242, 244), (240, 245, 241), (202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

# initialize the object attributes and x-y position
x = -125
y = -125
row = 1
column = 1
the_mighty_turtle = Turtle()
the_mighty_turtle.penup()
the_mighty_turtle.goto(x, y)
the_mighty_turtle.hideturtle()
the_mighty_turtle.speed("fastest")

for column in range(1, 11):
    for row in range(1, 11):
        the_mighty_turtle.dot(15, random.choice(pen_colors))
        x += 30
        the_mighty_turtle.goto(x, y)
    x = -125
    y += 30
    the_mighty_turtle.goto(x, y)

the_majesty_screen = Screen()
the_majesty_screen.exitonclick()
