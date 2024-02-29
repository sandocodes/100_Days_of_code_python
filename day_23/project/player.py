from turtle import Turtle

# Constant Variables
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """Player class"""
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def move_forward(self):
        """Move turtle forward with the press of the "up" key."""
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        """Bring the turtle back to its starting position each time it crosses to the other side."""
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        """Detect if the player makes it to the finish line."""
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
