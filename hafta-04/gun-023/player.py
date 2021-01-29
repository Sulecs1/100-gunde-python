from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle") # oyuncu şekli
        self.penup() # çizim yapmayacak
        self.go_to_start() # oyunun başlama noktası
        self.setheading(90) # şeklin yönü

    def go_up(self):
        self.forward(MOVE_DISTANCE) # belirtilen piksel kadar ileriye gidecek

    def go_to_start(self):
        self.goto(STARTING_POSITION) # başlangıç noktasını belirleyen metot.

    def is_at_finish_line(self):
        # kaplumbağanın bitiş noktasına başarılı bir şekilde geçişini sorgulayan metot.
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
