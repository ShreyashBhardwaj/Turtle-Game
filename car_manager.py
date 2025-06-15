from turtle import  Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        random_number=random.randint(0, len(COLORS)-1)
        self.color(COLORS[random_number])
        self.penup()
        self.y_move=random.randint(-270,280)
        self.x_move=STARTING_MOVE_DISTANCE
        self.move_speed=10

    def car_move(self):
        self.goto(x=(self.xcor()+self.x_move),y=self.y_move)

    def level_up(self):
        self.x_move+=MOVE_INCREMENT

    def reset_position(self):
        self.goto(310,self.y_move)
        self.level_up()
