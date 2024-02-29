import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Player
player = Player()
car_manager = CarManager()

# Listen for Up button press to Move Player
screen.listen()
screen.onkey(player.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(car_manager.car_speed)
    screen.update()

    # CARS
    car_manager.create_car()
    car_manager.move_cars()

    # Detect Cars and Turtle collision (Game Over)
    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            game_is_on = False
            print("Game Over")

    # Detect when the Turtle crosses to the other side
    if player.is_at_finish_line():
        # Bring Player back to Starting Position
        player.go_to_start()

        # Increase Car Speed by Leveling Up
        car_manager.level_up()

screen.exitonclick()
