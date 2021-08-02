import time
from turtle import Screen
from food import Food
from scoreboard import ScoreBoard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Entangled Snake")
screen.tracer(0)  # turn off the tracer, until we call update() to refresh the screen

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()  # start listen for keystroke
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True
while game_is_on:
    screen.update()  # outside loop, screen only updates after moving all snake segments
    time.sleep(0.1)  # add 0.1 second delay after each segment moves
    snake.move()

    # Detect collision with food:
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detect collision with wall:
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        # game_is_on = False
        score.reset_scoreboard()
        snake.reset()

    # Detect collision with tail:
    for segment in snake.segments[1:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            # game_is_on = False
            score.reset_scoreboard()
            snake.reset()

screen.exitonclick()
