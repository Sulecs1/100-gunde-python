from turtle import Turtle

FONT = ("Courier", 18, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.color("white")
        self.goto(0, 270)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

