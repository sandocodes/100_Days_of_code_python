# Create Pong Game
from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()
# Screen Setup
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((-350, 0))
l_paddle = Paddle((-350, 0))


# Go Up function
def go_up(self):
    new_y = self.paddle.ycor() + 20
    self.paddle.goto(self.paddle.xcor(), new_y)


# Go Down function
def go_down(self):
    new_y = self.paddle.ycor() - 20
    self.paddle.goto(self.paddle.xcor(), new_y)


# Move Paddle Up and Down
screen.listen()
screen.onkey(Paddle((-350, 0)).go_up, "Up")
screen.onkey(Paddle((-350, 0)).go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
