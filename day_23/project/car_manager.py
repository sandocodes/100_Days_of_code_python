from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()

    def create_cars(self):
        for _ in range(10):
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=2, stretch_len=4)
            new_car.penup()
            new_car.goto(random.randint(0, 200), random.randint(-200, 200))

            new_car.forward(STARTING_MOVE_DISTANCE)
