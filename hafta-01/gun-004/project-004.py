# Taş - Kağıt - Makas!
# Bilgisayara karşı taş kağıt makas oyunu geliştirelim!
# Kuralları aşağıda belirttim.
# Taş makası yener.
# Makas kağıdı yener.
# Kağıt taşı yener.

import random

# Taş, Kağıt, Makas hareketleri oluşturuldu.

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Oyuncular oluşturuldu!
user = [rock, paper, scissors]
cpu = user.copy()

# Kullanıcıdan veri alındı

selection = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Eğer girilen değer 3'ten fazla veya 0'dan az ise ise oyunu bitir.
if selection >= 3 or selection < 0:
    print("You typed an invaild number, you lose!")
else:
    # Oyun oynandı ve seçimler elde edildi
    user_select = user[selection]
    cpu_select = cpu[random.randint(0, 2)]
    print(user_select)
    print(f"Computer choose:\n{cpu_select}")

    if user_select == user[0] and cpu_select == cpu[0]:
        print("Draw.") # taş - taş
    elif user_select == user[0] and cpu_select == cpu[1]:
        print("You Lose.") # taş - kağıt
    elif user_select == user[0] and cpu_select == cpu[2]:
        print("You Won.") # taş - makas
    elif user_select == user[1] and cpu_select == cpu[0]:
        print("You Won.") # kağıt - taş
    elif user_select == user[1] and cpu_select == cpu[1]:
        print("Draw.") # kağıt - kağıt
    elif user_select == user[1] and cpu_select == cpu[2]:
        print("You Lose.") # kağıt - makas
    elif user_select == user[2] and cpu_select == cpu[0]:
        print("You Lose.") # makas - taş
    elif user_select == user[2] and cpu_select == cpu[1]:
        print("You Won.") # makas - kağıt
    elif user_select == user[2] and cpu_select == cpu[2]:
        print("Draw.") # makas - makas

print("-")