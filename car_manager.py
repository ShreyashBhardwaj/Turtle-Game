from turtle import  Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars=[]
        self.create_car()


    def create_car(self):
        new_car=Turtle()
        new_car.shape("square")
        random_number = random.randint(0, len(COLORS) - 1)
        new_car.y_pos = random.randint(-275, 275)
        new_car.color(COLORS[random_number])
        new_car.penup()
        new_car.goto(x=281, y=new_car.y_pos)
        new_car.move_speed = STARTING_MOVE_DISTANCE
        self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.goto((car.xcor()-car.move_speed),car.ycor())

        self.all_cars = [car for car in self.all_cars if car.xcor() > -320]

    def level_up(self):
        for car in self.all_cars:
            car.move_speed+=MOVE_INCREMENT

    def reset_position(self):
        for car in self.all_cars:
            self.goto(310,(car.y_pos+random.randint(0,10)))
            self.level_up()
