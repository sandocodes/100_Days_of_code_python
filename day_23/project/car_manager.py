from turtle import Turtle
import random

# Constant Variables
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_SPEED = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        """Car Manager class local variables"""
        self.all_cars = []
        self.car_speed = STARTING_MOVE_SPEED

    def create_car(self):
        """Create a new car with random color every time the game loops 6 times."""
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    # Move Cars across the screen
    def move_cars(self):
        """Move the cars across the screen"""
        for car in self.all_cars:
            car.backward(self.car_speed)

    # Increase Car Speed
    def level_up(self):
        """Increase the car speed when the car crosses to the other side."""
        self.car_speed += MOVE_INCREMENT
