from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.penup()
        self.goto(x_pos, y_pos)
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=0.8)
        self.color("white")

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
