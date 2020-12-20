# Higher Lower oyunu
# Oyunun oynanma amacını http://www.higherlowergame.com/ adresinden öğrenebilirsiniz.
# Buradaki oyun mantığını Instagram takipçi sayısı üzerinden oluşturdum.
# Bu bölüm de projeyi bakmadan geliştireceğim.

#### Yapılacaklar ####

# 1. Logoyu ekrana yazdır.
# 2. Ragele olacak şekilde A ve B seçeneklerini oluştur.
# 3. Seeçenek doğru seçildiğinde skor artımı yap.
# 4. B seçeneğini A seçeneğine taşı ve B seçeneğini rasgele oluştur.
# 5. Yanlış seçenek seçilene kadar 3. ve 4. adımları gerçekleştir.

#### İş Akışı ####

# https://bit.ly/38jkX27

#### Kodlar ####

import random
import art
import data
import pyautogui


def choose_data(data):
    return random.choice(data)


def questions(opt1, opt2):
    if opt1 == opt2:
        opt2 = choose_data(data.data)
    else:
        print(f"Pssst! Test your code. A: {opt1['follower_count']}, B: {opt2['follower_count']}")
        print(f"Compare A: {opt1['name']}, {opt1['description']}, from {opt1['country']}.")
        print(art.vs)
        print(f"Against B: {opt2['name']}, {opt2['description']}, from {opt2['country']}.")
        answer = input("Who has more followers? Type 'A' or 'B': ").upper()
        if answer == "A":
            if opt1["follower_count"] > opt2["follower_count"]:
                return True
            else:
                return False
        elif answer == "B":
            if opt2["follower_count"] > opt1["follower_count"]:
                return True
            else:
                return False
        else:
            return False


print(art.logo)

score = 0
is_game_over = False
a = choose_data(data.data)
b = choose_data(data.data)

while not is_game_over:
    if questions(a, b):
        score += 1
        print(f"You're right! Current score: {score}.")
        a = b
        b = choose_data(data.data)
    else:
        is_game_over = True
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")