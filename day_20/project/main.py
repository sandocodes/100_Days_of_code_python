# Snake Game
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard, FONT
import time

tur = Turtle()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Listen of keystrokes (Up, Down, Left and Right)
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# (2) Move the Snake Forward
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.snake_head.distance(food) < 15:
        food.food_refresh()
        snake.extend()
        # Update the score when the snake eats the food
        scoreboard.increase_score()

    # Detect collision with the wall to end the game.
    if (snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280 or snake.snake_head.xcor() > 280 or snake.
            snake_head.xcor() < -280):
        game_is_on = False
        scoreboard.game_over()

    # Detect tail collision
    for segment in snake.segments[1:]:
        # If the head collides with any segment in the tail, trigger game over.
        if snake.snake_head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
