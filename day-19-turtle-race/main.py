# Instances, State and Higher Order Functions

from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)  # set the canvas size
colors = ["red", "orange", "blue", "yellow", "green", "purple"]
all_turtles = []

x = -230
y = -120
distance = 0

for i in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(i)
    new_turtle.goto(x, y)
    y += 50
    all_turtles.append(new_turtle)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_speed = random.randint(0, 20)
        turtle.forward(random_speed)


screen.exitonclick()
