from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)  # animasyonu durdur
screen.bgcolor("black")
screen.title("My Snake Game")

snake = Snake()
food = Food()
score = ScoreBoard()

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

    # yılan yemeği yediğinde yapılacaklar
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # yılan duvara çarptığında yapılacaklar
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score.game_over()

    # yılan kendi bedenine çarprığında yapılacaklar

    for segment in snake.segments[1:]:
        # for içerisinde dönen segmentlerin ilki yılanın baş kısmı olduğundan mantıksal hataya düşmemek için
        # ilk segmenti pas geçtik
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
