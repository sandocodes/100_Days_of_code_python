from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")
DATA_PATH = "./data.txt"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open(DATA_PATH) as data:
            self.high_score = int(data.read())
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.write_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(DATA_PATH, "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.write_score()
