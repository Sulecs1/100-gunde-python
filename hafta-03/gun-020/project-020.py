from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)  # animasyonu durdur
screen.bgcolor("black")
screen.title("My Snake Game")

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()  # animasyonu güncelle
    time.sleep(0.1)

    snake.move()







screen.exitonclick()
