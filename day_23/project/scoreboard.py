from turtle import Turtle

# Constant Variables
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        """Scoreboard class local variables"""
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(-280, 270)
        self.hideturtle()
        self.display_level()

    # Write Level
    def display_level(self):
        """Display Game Level on the screen (upper-left corner)"""
        self.color("black")
        self.write(f"Level: {self.level}", False, align="left", font=FONT)

    # Update Level
    def update_level(self):
        """ Increases Level each time turtle makes it across."""
        self.level += 1
        self.clear()
        self.display_level()

    def game_over(self):
        """Display "Game Over" when the turtle collides with any of the cars."""
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=FONT)
