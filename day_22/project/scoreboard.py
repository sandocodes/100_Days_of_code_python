from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.write(f"{self.l_score} - {self.r_score}", font=FONT, align=ALIGNMENT)

    def right_score(self):
        self.r_score += 1
        self.clear()
        self.write_score()

    def left_score(self):
        self.l_score += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over", font=FONT, align=ALIGNMENT)

