from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = [] # rasgele oluşturulan arabaların tutulacak listesi
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6) # 1-6 arası rassal sayı üret
        if random_chance == 1:
            # eğer rassal sayı 1'e eşit olursa araba çıkar. Değilse araba çıkarma.
            # Çünkü çok fazla araba çıkar ve oyun zordan başlar.
            new_car = Turtle("square") # arabanın şekli
            new_car.shapesize(stretch_wid=1, stretch_len=2) # yükseklik ve genişlik bilgisi
            new_car.penup() # çizim yapmayacak
            new_car.color(random.choice(COLORS)) # belirtilen renklerden rasgele seçilecek
            random_y = random.randint(-250, 250) # yatay boyunca edineceği konum.
            # 30 piksel üstten 30 piksel alttan oyuncuya alan bırakılacak.
            new_car.goto(300, random_y) # arabanın başlangıç konumu
            self.all_cars.append(new_car) # oluşturulan araba listeye eklendi

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE) # listedeki herbir araba belirtilen piksel değeri kadar geriye hareket edecek

    def level_up(self):
        self.car_speed += MOVE_INCREMENT # eğer kaplumbağa karşıya başarılı bir şekilde geçerse hareket hızını artır.
