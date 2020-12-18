############DEBUGGING#####################

# Debugging işlemi, program içerisindeki hataları ayıklamak için kullanılan yöntemdir.
# Herkes programda hata yapabilir. Programlamada hata yapmak gelişmenin iyi yollarından biridir.
# Debugging işlemi için belli başlı tüyolar mevcut

# %%

###### PROBLEMİ TANIMLA ######

# Problemin nerede olduğunu anla. Eğer problemin tam olarak nerede olduğunu anlayamazsan debug etme işlemini yapamazsın.
# Bu gibi durumlarda birtakım sorular sorman gerekebilir. Bu konu için örnek soruları listeleyecek olursak:

# * For döngüsü neye yarıyor?
# * Fonksiyon nerede "You got it" ifadesini yazdırıyor?
# * i değişkeni hangi değerleri alıyor?

# Hatalı Kod

def my_function():
    for i in range(1, 20):  # range fonksiyonu 20 değerini dahil etmez.
        if i == 20:
            print("You got it") # bu yüzden bu ifade ekrana yazılmaz.
my_function()

# %%

def my_function():
    for i in range(1, 21):  # 20 değerini 21 ile değiştirdik.
        if i == 20:
            print("You got it")
my_function()

# %%

###### HATAYI KENDİN ÜRET ######

# Çıkan hatayı yeniden üret. Çünkü hatayı yeniden üretmek çözüme giden yol olabilir.

from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)  # randint metodu 6 değerini de dahil eder. Bunu test etmek için her bir değeri denemek gerekebilir (1, 2, 3, 4, 5, 6)
print(dice_imgs[dice_num])

# %%

from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)  # listenin indeks yapısına göre çözüldü.
print(dice_imgs[dice_num])

# %%

###### EMPATİ KUR ######

# Aslında konu bilgisayarın çalışma mantığı ile düşünmekten geçiyor.
# Burada bilgisayar gibi düşünerek verilen değeri yerlerine tek tek koyman gerekir.

year = int(input("What's your year of birth?"))  # 1994 dediğimizi düşünelim
if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year > 1994:
    print("You are a Gen Z.")

# %%

year = 1994
if 1994 > 1980 and 1994 < 1994:
    print("You are a millenial.")
elif 1994 > 1994:
    print("You are a Gen Z.")

# %%

year = 1994
if True and False:
    print("You are a millenial.")
elif False:
    print("You are a Gen Z.")

# iki seçenekte de False olduğu için bir çıktı vermedi

# %%

year = int(input("What's your year of birth?"))  # 1994 dediğimizi düşünelim
if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year >= 1994:  # eşittir ifadesi ekledik.
    print("You are a Gen Z.")

# %%

###### HATALARI DÜZELT ######

# Söz dizimi hatası, konsol hatası ve mantıksal hataları bul ve düzelt.

age = input("How old are you?")
if age > 18:
print("You can drive at age {age}.") # girinti oluştur

# %%

age = input("How old are you?")  # int tipine çevir
if age > 18:
    print("You can drive at age {age}.")

# %%

age = int(input("How old are you?"))
if age > 18:
    print("You can drive at age {age}.") # f-String kullan

# %%

age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")

# %%

###### PRINT SENİN EN İYİ ARKADAŞIN ######

# Eğer çok sıkıştığını düşünüyorsan sıkıştığın noktada print fonksiyonunu kullan.

pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: ")) # 4. çünkü eşit sorgusu konulmuş.
total_words = pages * word_per_page # 1. burada istenen sonucu alamıyoruz. Bu yüzden print fonksiyonu ile değerleri soralım
print(f"pages = {pages}") # 2. girdiğimiz değere eşit
print(f"word_per_page = {word_per_page}") # 3. girdiğimiz değere eşit değil
print(total_words)

# %%

pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(f"pages = {pages}")
print(f"word_per_page = {word_per_page}") l
print(total_words)

# %%

###### DEBUGGER ARACINI KULLAN ######

# Tonny veya PythonTutor aracını kullanabilirsin.

def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
    b_list.append(new_item) # 2. tek tek incelendiğinde bu ifadenin girinti olması gerekiyor.
    print(b_list)

mutate([1,2,3,5,8,13])  # 1. ekrana [26] değeri veriyor.

# %%

def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)

mutate([1,2,3,5,8,13])

# %%

###### DİĞER HATA AYIKLAMA ÖNERİLERİ ######

# ara ver: bazı noktalarda sürekli işin içerisinde olduğun için hataları doğru olarak kabul edebilirsin. Biraz hava al, ara verip başka işe geç veya bir gün üzerine yat. Sonrasında ise tekrar projen üzerinde çalış.
# Arkadaşlarına sor: bazen dışarıdan bakan birinin katkısı olabilir. Bu gibi durumlarda daha hızlı hata çözülebilir.
# Her düzeltmenin sonucunda yeniden çalıştır: ufak bile olsa her düzenlemenden sonra programı çalıştırmak hatayı adım adım çözmeyi sağlayabilir.
# StackOverflow adresinde ara: senden önce hatayla kesin biri uğraşmıştır. Kişiyi bul ve sorunun cevabını çözmeye çalış.