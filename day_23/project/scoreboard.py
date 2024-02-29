from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(-275, 270)
        self.hideturtle()
        self.display_level()

    # Write Level
    def display_level(self):
        self.color("black")
        self.write(f"Level: {self.level}", True, align="left", font=FONT)

    # Update Level
    def update_level(self):
        self.level += 1
        self.clear()
        self.display_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align='center', font=FONT)
