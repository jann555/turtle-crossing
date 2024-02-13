from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.garage = []

    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.penup()
            self.setheading(180)
            new_car.shape("square")
            new_car.color(choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(300, randint(-250, 250))
            self.garage.append(new_car)

    def move_cars(self):
        for car in self.garage:
            car.back(STARTING_MOVE_DISTANCE)
