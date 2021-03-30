from turtle import Turtle
import random

RIGHT_ANGLE = [*range(1, 76), *range(385, 360)]
LEFT_ANGLE = [*range(105, 179), *range(181, 255)]
ALL_ANGLES = RIGHT_ANGLE + LEFT_ANGLE
ANGLE = random.choice(ALL_ANGLES)


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("red")
        self.move_speed = 0.1

    def move(self):
        global ANGLE
        self.setheading(ANGLE)
        self.forward(20)

    def bounce_wall(self):
        global ANGLE
        ANGLE = 360 - ANGLE
        self.setheading(ANGLE)

    def bounce_paddle(self):
        global ANGLE
        ANGLE = 180 - ANGLE
        self.setheading(ANGLE)
        self.move_speed *= 0.9

    def reset_position(self):
        global ANGLE
        self.goto(0, 0)
        self.move_speed = 0.1
        if ANGLE in range(90, 271):
            ANGLE = random.choice(RIGHT_ANGLE)
        else:
            ANGLE = random.choice(LEFT_ANGLE)
        self.setheading(ANGLE)
