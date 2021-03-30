from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 200)
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.l_score} {self.r_score}", align="center", font=("Courier", 88, "normal"))

    def increase_l(self):
        self.l_score += 1
        self.update_scoreboard()

    def increase_r(self):
        self.r_score += 1
        self.update_scoreboard()
