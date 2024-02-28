import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Temp import
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create cars
rand_position_x = random.randint(1, 5)
rand_position_y = random.randint(1, 5)
position = (rand_position_x, rand_position_y)
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
cars = []

for car in range(len(COLORS)):
    new_car = Turtle("square")
    new_car.color(random.choice(COLORS))
    new_car.goto(position)


#########################################
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()



screen.exitonclick