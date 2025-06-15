import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

score = Scoreboard()

player=Player()

# Listen for key presses
screen.listen()
screen.onkeypress(player.player_move, "Up")
car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars()
    if random.randint(1, 6) == 1 :  # ~16% chance each loop
        car_manager.create_car()

    if player.ycor()>=270:
        player.reset_position()
        car_manager.level_up()
        score.update()

    for car in car_manager.all_cars:
        if player.distance(car)<20:
            score.game_over()
            game_is_on=False
            screen.exitonclick()
