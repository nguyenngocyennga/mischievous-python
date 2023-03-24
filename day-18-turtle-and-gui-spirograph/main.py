# Graphical User Interface (GUI)

from turtle import Turtle, Screen
import random
import turtle as turtle

t = Turtle()
t.shape("arrow")
# t.pensize(1)
t.speed("fastest")
turtle.colormode(255)

# side = 3
# pen_colors = ["cyan", "dodger blue", "tomato", "medium violet red", "hot pink", "forest green", "light sea green",
#               "dark orange", "cornflower blue", "pale violet red", "deep pink"]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    generated_color = (r, g, b)
    return generated_color


orientations = [0, 90, 180, 270]
i = 0

while i < 360:
    # t.color(random.choice(pen_colors))
    t.setheading(i)
    t.color(random_color())
    # t.forward(20)
    t.circle(100, 360, 9)
    i += 5


# while side < 11:
#     left_angle = 360 / side
#     t.pencolor(random.choice(pen_colors))
#     for _ in range(side):
#         t.forward(100)
#         t.left(left_angle)
#     side += 1

# for i in range(4):
#     for _ in range(25):
#         t.pendown()
#         t.forward(4)
#         t.penup()
#         t.forward(4)
#     t.left(90)

my_screen = Screen()
my_screen.exitonclick()
