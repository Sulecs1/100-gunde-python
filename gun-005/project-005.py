# Password Generator Project
# Burada amaç, tanımlanan harfler, sayılar ve sembolleri kullanarak rasgele parolalar oluşturmak.
# Parola oluşturulurken kişilere oluşturmak istedikleri parolaların kaç harften, sembolden ve sayıdan oluşturmak istediğini sormak.
# Program iki seviyeden oluşuyor.
# 1. Seviye kolay bir seviye. Karışık sıra olmadan önce harfler, sonra semboller ve sonrasında da sayılar kullanılıyor. (Örnek: JduE&!91)
# 2. Seviye biraz daha zor bir seviye. Hem karakterler rasgele hem de oluşturulma sıraları rasgele (Örnek: g^2jk8&P)

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password1 = ""

for i in range(nr_letters):
    password1 += letters[random.randint(0, len(letters)-1)]

for i in range(nr_symbols):
    password1 += symbols[random.randint(0, len(symbols)-1)]

for i in range(nr_numbers):
    password1 += numbers[random.randint(0, len(numbers)-1)]

print(f"Here is your password: {password1}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password2 = ""

for i in range(nr_letters):
    password2 += random.choice(letters) # yukarıdaki kodun bir alternatifi

for i in range(nr_symbols):
    password2 += random.choice(symbols)

for i in range(nr_numbers):
    password2 += random.choice(numbers)

password2 = "".join(random.sample(password2, len(password2)))

print(f"Here is your password: {password2}")