import turtle as turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


# Keystrokes:
# W = Forwards
# S = Backwards
# A = Counter-Clockwise
# D = Clockwise


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def rotate_counter_clockwise():
    tim.right(10)


def rotate_clockwise():
    tim.left(10)


def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()  # tell the screen to start listening
screen.onkey(key="d", fun=move_forward)  # function move_forward() is passed as argument, so no parentheses
screen.onkey(key="a", fun=move_backward)
screen.onkey(key="w", fun=rotate_counter_clockwise)
screen.onkey(key="s", fun=rotate_clockwise)
screen.onkey(key="c", fun=clear_drawing)

screen.exitonclick()
