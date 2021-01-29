from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1 # seviye başlangıcı
        self.hideturtle() # turtle nesnesi gizlendi
        self.penup() # çizim olmayacağı için kalem gizlendi
        self.goto(-280, 250) # başlangıç noktası
        self.update_scoreboard()

    def update_scoreboard(self):
        # seviye yazısını güncelleyen metot
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        # seviye değerini artıran metot
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        # oyun bittiğinde ekrana yazılacak mesajın metodu
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

