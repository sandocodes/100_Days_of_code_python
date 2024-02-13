from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

    def score_update(self):
        self.score += 1
        print(f"Score is now: {self.score}")
        self.write(f"Score: {self.score}", False, align="center")
