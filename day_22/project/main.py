# Create Pong Game
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
# Screen Setup
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Move Paddle Up and Down
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with top or bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with the paddle(s)
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_score()
        if scoreboard.l_score == 10:
            game_is_on = False
            scoreboard.game_over()
    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_score()
        if scoreboard.r_score == 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
