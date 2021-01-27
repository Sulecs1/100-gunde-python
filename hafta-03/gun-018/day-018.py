# Turtle Kütüphanesi

# Giriş: Turtle Kütüphanesi çeşitli grafiksel işlemleri yapmamızı sağlayan bir araçtır.

from turtle import Turtle, Screen
import random

tim = Turtle()

def my_random_color():
    R = random.random()
    G = random.random()
    B = random.random()
    tim.pencolor(R, G, B)

# Giriş Kodları
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

# CH-1: Kare Çiz

# for _ in range(4):
#     tim.right(90)
#     tim.forward(100)

# CH-2: Kesik çizgi çiz

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# CH-3: İç içe çokgen çiz


# for diagonal in range(3, 11):
#     my_random_color()
#     for _ in range(diagonal):
#         tim.forward(100)
#         tim.right(360 / diagonal)

# CH-4: Random Walk

# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")
#
# for _ in range(200):
#     my_random_color()
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# CH-5: Spirograph Çiz

step = 100
angle = 0
tim.speed("fastest")

while angle <= 360:
    my_random_color()
    tim.circle(100)
    angle += 360 / step
    tim.setheading(angle)

my_screen = Screen()
my_screen.exitonclick()


