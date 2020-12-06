# %%

## Rasgelelik
# Programlamada rassallık önemli bir yere sahip.
# Özellikle bu rassallığı oyunlarda görürüz.
# Deterministik sistemlerde (bilgisayarlarda) hangi girdinin hangi çıktıyı vereceği bellidir.
# Skotastik sistemlerde ise girdinin vereceği çıktı belli değildir ve bu durumu rasgelelil veya rassallık olarak adlandırabiliriz.
# Python'da rasgelelik Mersenne Twister algoritması ile oluşturulur (Detay için WikiPedia başlangıç olabilir.)
# Python'da rasgele sayı oluşturmak için random modülü kullanılabilir. askpython.com adresinden modüller hakkında bilgi alabilirsiniz.

# %%

import random

random_integer = random.randint(1, 10) # rasgele tamsayı üretir 1 ve 10 dahil
print(random_integer)

# %%

## Modül Nedir?
# Modül karmaşık programlar kurabilmek için başkaların ürettiği programlardan faydalanmaktır.
# Örnek olarak random modülü Python geliştiricileri tarafından geliştirildi ve kendi projemizde çağırıp kullanabiliyoruz. Eğer bu modül geliştirilmeseydi her rasgele sayı üretme ihtiyacımız olduğunda Mersenne Twister algoritmasını kendimiz yazmak zorunda kalabilirdik.
# Python'da modül oluşturmak basit. Aynı dizin altında modül oluşturmak için my_module.py adında bir dosya oluşturdum ve içerisinde bir değişken oluşturdum.
# Aşağıda ise bu modülü buradaki dosyaya import ettim.

import my_module # kendi modülümü yazdım.

print(my_module.pi) # içerisindeki değeri çağırdım.

# %%

random_float = random.random() # rasgele ondalık sayı üretir (0 dahil 1 dahil değil).
print(random_float)

# Soru: 0-5 arasında rasgele ondalık sayı nasıl üretilir?

print(random_float * 5) # Cevap

# %%

## Listeler
# Listeler bir veri yapısıdır.
# Veri yapısı ne demektir? Veri yapısı düzenli ve organize şekilde verileri saklamanın yoludur.
# Tek bir veri saklamak istediğimizde tek değişken oluştururuz.
# Birden fazla birbirine benzer değerleri saklamak için ise listeler kullanılır.
# Listelerin yapısı basittir.

fruits = ["apple", "orange", "pear", "cherry"]

# Köşeli parantezler içerisinde yazılır ve farklı veri tiplerini (int, str, bool, float) içinde barındırır.

# %%

# Liselerde eleman seçim işlemi için köşeli parantez kullanılır.

print(fruits[0]) # 1. eleman
print(fruits[2]) # 3. eleman

# Indexler neden 0'dan başlar?
#
#          |   
# fruits = | ["apple", "orange", "pear", "cherry"]
#          |     0         1        2        3
#
# Yukarıdaki şekilde bir çizgi çizdiğimizi düşünürsek apple değeri çizgiye 0 birim uzaklıkta, orange değeri 1, pear değeri 2 ve cherry değeri 3 birim uzaklıkta. Bu yüzden programlama dillerinde indexler 0 ile başlar.

# %%

# İndeksler pozitif olabileceği gibi negatif de olabilirler ve -1 ile başlayarak azalırlar.

print(fruits[-1]) # 4. eleman
print(fruits[-2]) # 3. eleman

# %%

# Listeler değiştirilebilir yapıya sahiptir.

fruits[2] = "grape"
print(fruits)

# %%

# Listelerin sonuna eleman eklemek için append() metodu kullanılır.

fruits.append("mango")
print(fruits)

# %%

# Eklemen istenen eleman bir değil de birden fazla ise extend() metodu kullanılır.

fruits.extend(["watermelon", "peach"])
print(fruits)

# %%

## IndexError

# Liste elemanı seçim işleminde indeks sayısından fazla yazılıyor ise IndexError hatası alınır.

print(fruits[len(fruits)]) # indeks değeri toplam eleman sayısı kadar.

# %%

# Bu hatayı düzeltmek için bir eksiğini almak yeterli olur.

print(fruits[len(fruits) - 1])

# %%

## İç İçe Listeler

# Python'da listeler iç içe oluşturulabilir.

liste1 = [1, 2, 3]
liste2 = [3, 4, 5]
tum_liste = [liste1, liste2]
print(tum_liste)

# 4 değerini seçmek için aşağıdaki komut kullanılır.

print(tum_liste[1][1]) # 1. indekse sahip lisyeyi seç ve 1. indekse sahip elemanı getir.