from turtle import Turtle
import random


class Food(Turtle):  # Food class has all capabilities of Turtle class
    # and also its own specific behaviours

    def __init__(self):  # whenever you initialize a new food object
        # from the food class, the init gets called
        super().__init__()  # add in super class call
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
