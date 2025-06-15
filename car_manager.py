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
        self.y_pos=random.randint(-275,275)
        self.color(COLORS[random_number])
        self.penup()
        self.goto(x=281,y=self.y_pos)
        self.move_speed=STARTING_MOVE_DISTANCE

    def car_move(self):
        self.goto(x=(self.xcor()+self.move_speed),y=self.y_pos)

    def level_up(self):
        self.move_speed+=MOVE_INCREMENT

    def reset_position(self):
        self.goto(310,(self.y_pos+random.randint(0,10)))
        self.level_up()
