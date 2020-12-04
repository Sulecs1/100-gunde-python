#%%

# Ekrana yazdırılmasını istediğimiz ifadeler için print() fonksiyonu kullanılır.

print("Hello World")

#%%

# Çift tırnak içerisinde yazdırılan ifadelere Python'da String adı verilir.

"Hello World"

#%%

# Eğer sonda bir çift tırnak unutuluar ise Python hata verir. Hata veren kodları yorum satırına alıyorum.

# print("Hello World)

#%%

# Bir önceki bölümde alınan hata mesajı aşağıdadır. Bu mesajı Google'da aratarak çözümünü bulabilirsin.
# SyntaxError: EOL while scanning string literal
# Programlamada birden çok hata alırız ve bu hatalar ile mücadele ederiz.

#%%

# Bir string ifadeyi birden fazla alt alta yazmak için aşağıdaki yöntem uygulanabilir.
print("Hello World!")
print("Hello World!")
print("Hello World!")

#%%

# Yukarıdaki işlemi yapmak yerine aşağıdaki işlem de yapılabilir.
print("Hello World!\nHello World!\nHello World!")

#%%

# Python'da birden fazla string ifadeler birleştirilebilir.
print("Hello" + "Cemal") # HelloCemal

#%%

# Yukarıdaki işlemin arasında boşluk eklemek için aşağıdaki işlem yapılabilir.
print("Hello" + " " + "Cemal") # Hello Cemal

#%%

# input() fonksiyonu dışarıdan veri almamızı sağlar. Kodun mantığını anlamak için belirtilen gif dosyasını izle.
print("Hello " + input("What is your name?\n")) # day-001-debug.gif

#%%

# Değişkenler, veriyi niteleyen isimlerdir.
name = input("What is your name?")
print(name)

#%%

# Değişkenlere ait veriler program akışı içerisinde değiştirilebilir.
name = "Jack"
print(name)

name = "Angela"
print(name)

#%%

# Dışarıdan alınan ismin kaç harften oluştuğunu ekrana yazdır.
print(len(input("What is your name? ")))

#%%

# Yukarıdaki işlemi değişken kullanarak yap.
name = input("What is your name? ") # klavyeden alınan ismi tutar
length = len(name) # ismin uzunluğunu tutar
print(length) # uzunluk yazdırılır

#%%

# Değişken oluşturma ile ilgili dikkat edilecek noktalar:
# Kodun okunabilir olmalı.
# Değişken ismin birden fazla kelime içeriyorsa alt çizgi ile ayır.
# Değişken ismi sayı ile başlayamaz.
# Değişken isimleri çağrılırken bire bir çağrılmalıdır.