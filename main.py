import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#Todo-1 Create the movement of the cars
#Todo-2 Create the player Movement
#Todo-3 When player hits 280 ensure that it goes back to -280 and increase the speed of car


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Listen for key presses
screen.listen()
#screen.onkeypress(paddle_right.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car = CarManager()

