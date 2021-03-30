import time
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
# TODO: [v] Create a scoreboard
scoreboard = Scoreboard()

# TODO: [v] Move the turtle with keypress:
screen.listen()
screen.onkey(key="Up", fun=player.go_up)

game_is_one = True
while game_is_one:
    time.sleep(0.1)
    screen.update()

    # TODO: [v] Create and move the cars:
    car_manager.create_car()
    car_manager.move_cars()

    # TODO: [v] Detect collision with car:
    for car in car_manager.all_cars:
        if player.distance(car) < 25:
            game_is_one = False
            scoreboard.game_over()

    # TODO: [v] Detect when turtle reaches the other side:
    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.increase_level()
        car_manager.level_up()

screen.exitonclick()
