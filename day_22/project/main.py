# Create Pong Game
from turtle import Screen, Turtle
from paddles import Paddles
import time

pong = Turtle()
paddle = Paddles()

pong.hideturtle()
screen = Screen()
screen.tracer(0)
screen.setup(width=1200, height=600)
screen.bgcolor("black")
screen.title("Pong Game")

# Disable Animation


# Create Pong Board
pong.color("white")
pong.penup()
pong.setheading(90)
pong.goto(0, 307)
pong.setheading(270)

for _ in range(30):
    pong.forward(10)
    pong.penup()
    pong.forward(10)
    pong.pendown()

# Create Paddle

screen.update()
time.sleep(0.2)
screen.exitonclick()
