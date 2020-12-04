#%%

# Geçen bölümde kullanılan len fonksiyonuna sayı değerleri gönderildi ve tip hatası geriye döndü. Çünkü len tamsayılarda çalışmıyor.
# len(1214123)
# Ders esnasında verilen bir örnek tam olarak şuydu; Bir patates doğrama makinesini düşünün. İçerisine patates attığında size kızartmanız için doğranmış patates veriyor. Eğer bu makinenin içerisine patates yerine taş verirsek makine çalışmayacaktır. İşte bazı fonksiyonlara bazı değerler verildiğinde çalışmayabilir. Yukarıdaki örnek gibi.
# Bunun için Python'da temel veri tiplerini anlamak gerekebilir.
#%%

# String

"Hello" # çift tırnak arasına yazılan karakterlerdir.
"Hello" # sayılabilir bir veri tipidir.
"Hello"[0] # birinci karakteri seçmeyi sağlar ve programlamada sayma işlemi 0'dan başlar.

print("Hello"[0]) # H
print("Hello"[4]) # o

"123" # bu sayı değil stringtir.
print("123" + "345") # 123345 yazar

#%%

# Integer

123 # tamsayılardır.
print(123 + 345) # 468

print(123_456_789) # büyük sayıları ayırmak için alt çizgi kullanılır.

#%%

# Float

3.14159 # ondalık sayılardır.
print(3.14159)

#%%

# Boolean

# iki değer alır
True
False

# T ve F harfleri büyük olmalı
# Tırnaklar arasına yazılmamalıdır.

#%%

# Tip Hatası Örneği
# Bir önceki bölümde len ifadesinin integer ile çalışmadığı görüldü. Aynı şekilde integer ifadesi aşağıdaki örnekte de çalışmaz.

num_char = len(input("What's your name? "))
print("Your name has " + num_char + " characters.")

#%%

# Buradaki num_char değişkeninin değerini type fonksiyonu ile sorguluyoruz.
print(type(num_char))

#%%

# Yukarıdaki problemi çözmek için str fonksiyonunu kullanarak tip dönüşümü yapıyoruz.

num_char = len(input("What's your name? "))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

# Bunun yapılmasının nedeni bir tam sayı ile bir metinsel ifadenin birleştirme işleminin yapılamayacağını görmemizdi.

# %%

# Tip Dönüşümleri
# Tip dönüşümleri için aşağıdaki fonksiyonlar kullanılır.

int() # integer değerine dönüştürmek için
float() # float değerine dönüştürmek için
str() # string değerine dönüştürmek için

#%%

# Matematik Operatörleri

3 + 5 # toplama
7 - 3 # çıkarma
3 * 2 # çarpma
6 / 3 # bölme
2 ** 2 # üs alma

#%%

# Öncelik Sırası - PEMDASLR

# Parentheses --> Parantez
# Exponents --> Üs Alma
# Multiplication --> Çarpma
# Division --> Bölme
# Addition --> Toplama
# Subtraction --> Çıkarma
# LR --> Soldan Sağa

print(3 * 3 + 3 / 3 - 3) # day-002-debug.gif

#%%

# Sayı Manipülasyonu

# Sayı Yuvarlama

print(8 / 3) # Ondalık kısmı fazlasıyla uzun
print(round(8 / 3, 2)) # Ondalık kısım 2 basamağa yuvarlandı
print(8 // 3) # 8 değeri 3'e tam bölündü. Ancak burada yuvarlama işlemi olmadan ondalık kısım atıldı.

print(type(8 / 3))  # float
print(type(8 // 3)) # int

#%%

# Atama Operatörleri

result = 4 / 2 # değer atandı
result /= 2 # result = result / 2 işlemi yapıldı. Önce sağda işlem yapılır sonra sola atanır.
print(result) # 1.0

# += --> Artır Ata
# -= --> Azalt Ata
# *= --> Çarp Ata
# /= --> Böl Ata

#%%

# f-String --> Birbirinden farklı veri tiplerini birleştirmek için kullanılan pratik yol.

# f-String Bilmediğimizde
score = 0
height = 1.8
isWinning = True
print("your score is " + str(score) + ", your height is " + str(height) + ", you are winning is " + str(isWinning))

# f-String Bildiğimizde
print(f"your score is {score}, your height {height}, you are winning is {isWinning}")
