from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The majestic pong")
screen.tracer(0)  # turn off the animation

right_paddle = Paddle(360, 0)
left_paddle = Paddle(-360, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=right_paddle.go_up)
screen.onkey(key="Down", fun=right_paddle.go_down)
screen.onkey(key="q", fun=left_paddle.go_up)
screen.onkey(key="a", fun=left_paddle.go_down)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the wall:
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce:
        ball.bounce_wall()

    # Detect collision with the right paddle:
    if ball.xcor() > 330 and ball.distance(right_paddle) < 50 or ball.xcor() < -330 and ball.distance(left_paddle) < 50:
        ball.bounce_paddle()

    # Detect if the right paddle miss the ball:
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.increase_l()

    # Detect if the left paddle miss the ball:
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.increase_r()


screen.exitonclick()
