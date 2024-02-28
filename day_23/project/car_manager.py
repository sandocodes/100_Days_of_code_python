from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
    

    def create_cars(self):
        for _ in range(6):
            self.shape("square")
            self.color(random.choice(COLORS))
            self.shapesize(stretch_wid=2, stretch_len=4)
            self.goto(random.randint(0, 200), random.randint(-200, 200))
