# Sayı Tahmini Oyunu

# Bu projede yalnızım. Bu yüzden kendi yol haritamı çizmem gerekiyor. Gerekli notları burada paylaştım.
# En altta da bu notlara göre kodları bulabilrisiniz.

##### Program için yapılacak listem #####
# 1. Kendine Oyun Logosu Tasarla ve Ekrana Yazdır
# 2. Karşılama Mesajı yaz
# 3. Zorluk derecesi oluştur. Eğer kullanıcı kolay yolu seçer ise 10 hakkı olsun zor yolu seçer ise 5 hakkı olsun.
# 4. Rasgele bir sayı oluştur ve bunu bir değişkende sakla.
# 5. Kullanıcıdan bir sayı al ve oluşturulan sayı ile kontrolünü sağla.
# 6. Eğer tahmin edilen sayı olutşurulan sayıdan küçükse ekrana çok küçük, büyük ise çok büyük yaz.
# 7. Kullanıcıya zorluk derecesine göre bilemediği her cevap karşılığında kaç hakkı kaldığını yaz.
#    Bunu hak değeri 0 olana kadar yap.
# 8. Hak değeri 0 olduğunda ekrana oyunu kaybettiğini dile getir.
# 9. Tahmin edilen değer ile oluşturulan sayı birbirine eşit ise oyunu kazandığını dile getir.
# 10. Bu işlemleri fonksiyonel olarak yaz.

##### Program için iş akışı #####

# iş akışına buradan ulaşabilirsin
# https://bit.ly/2KzhGDC

##### Kodlama #####

import random

print("""
 _____  _____   _______   _____ ___   _   _ ___  ________ _   _ _____ 
/  ___|/ _ \ \ / /_   _| |_   _/ _ \ | | | ||  \/  |_   _| \ | |_   _|
\ `--./ /_\ \ V /  | |     | |/ /_\ \| |_| || .  . | | | |  \| | | |  
 `--. \  _  |\ /   | |     | ||  _  ||  _  || |\/| | | | | . ` | | |  
/\__/ / | | || |  _| |_    | || | | || | | || |  | |_| |_| |\  |_| |_ 
\____/\_| |_/\_/  \___/    \_/\_| |_/\_| |_/\_|  |_/\___/\_| \_/\___/ 

                                                             
""")

print("Sayı Tahmini Oyunuma Hoş Geldin!")
print("Bu oyundaki amaç 1-100 arasında tahmin edilen sayıyı bilmek!")

olusan_sayi = random.randint(1, 100)

zorluk_derecesi = input("Zorluk dereceni seç. 'kolay' veya 'zor': ").lower()

if zorluk_derecesi == "kolay":
    hak = 10
elif zorluk_derecesi == "zor":
    hak = 5
else:
    print("Hatalı değer girdiniz. Programı yeniden başlatın.")

oyun_bitti_mi = False

while not oyun_bitti_mi:
    tahmin_edilen_sayi = int(input("Bir sayı giriniz: "))
    if tahmin_edilen_sayi == olusan_sayi:
        print("Doğru bildin, tebrikler!")
        oyun_bitti_mi = True
    elif tahmin_edilen_sayi < olusan_sayi:
        hak -= 1
        if hak != -1:
            print(f"Çok Küçük.\nToplamda {hak+1} hakkın kaldı.")
        elif hak == -1:
            oyun_bitti_mi = True
    else:
        hak -= 1
        if hak != -1:
            print(f"Çok Büyük.\nToplamda {hak+1} hakkın kaldı.")
        elif hak == -1:
            oyun_bitti_mi = True

print(f"Hakkın kalmadı, kaybettin. Doğru cevap: {olusan_sayi}")
