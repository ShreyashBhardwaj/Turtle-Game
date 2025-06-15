from turtle import  Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    speed = STARTING_MOVE_DISTANCE
    def __init__(self):
        self.all_cars=[]
        self.create_car()
        self.speed=STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car=Turtle()
        new_car.shape("square")
        new_car.shapesize(stretch_wid=2,stretch_len=1)
        random_number = random.randint(0, len(COLORS) - 1)
        new_car.y_pos = random.randint(-290, 260)
        new_car.color(COLORS[random_number])
        new_car.penup()
        new_car.goto(x=290, y=new_car.y_pos)
        new_car.move_speed = self.speed
        self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.goto((car.xcor()-car.move_speed),car.ycor())

        self.all_cars = [car for car in self.all_cars if car.xcor() > -320]

    def level_up(self):
        self.speed+=MOVE_INCREMENT
        for car in self.all_cars:
            car.hideturtle()
        self.all_cars.clear()
