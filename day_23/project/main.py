import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager, COLORS
from scoreboard import Scoreboard
import random


car = CarManager()


screen = Screen()
screen.setup(width=600, height=600)
# screen.tracer(0)


# ########################## #

for _ in range(10):
    new_car = Turtle("square")
    new_car.color(random.choice(COLORS))
    new_car.shapesize(stretch_wid=2, stretch_len=4)
    new_car.penup()
    new_car.goto(random.randint(0, 200), random.randint(-200, 200))


# ########################## #



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    # screen.update()
    



screen.exitonclick