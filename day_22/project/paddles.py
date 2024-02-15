from turtle import Turtle

starting_positions = [(550, 0), (550, 20), (550, 40), (550, -20), (550, -40)]


class Paddles(Turtle):
    def __init__(self):
        super().__init__()
        self.paddle = []
        self.create_paddle()

    def create_paddle(self):
        for position in starting_positions:
            new_paddle = Turtle("square")
            new_paddle.color("white")
            new_paddle.penup()
            new_paddle.goto(position)

            self.paddle.append(new_paddle)
