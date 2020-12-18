# Global ve Local Etki Alanı

# Scope konusunu kısaca şuna benzetebiliriz, evinizin bahçesinde yetişen elma ağacındaki elmayı siz ve ailenizin yiyebilmesi durumu ile
# bahçenizin dışında yetişen elma ağacındaki elmayı herkesin yemesi durumuna scope denilerbilir.

# %%
# Local scope kavramı, fonksiyon içerisinde tanımlanan değişkenlerin etki alanıdır. Fonksiyon dışında çağrılamazlar.

b = 10 # global değişken


def etki_a():
    a = 100 # local değişken
    print(a)


etki_a()
print(b)

# %%

# Global scope kavramı, fonksiyon dışında oluşturulan değişkenlerdir.
# Bu değişkenler fonksiyon içerisinde çağrıldıklarında önce local scope alanında değişkeni ararlar sonrasında ise
# global scope alanında değişkeni ararlar ve bulduklarında istenen işlemi yaparlar.

b = 10 # global değişken


def etki_b():
    print(b)


etki_b()
print(b)

# Burada önemli nokta fonksiyon içerisinde çağırlan değişkenin fonksiyon yazılan yerden önce tanımlanıp tanımlanmadığıdır.
# Eğer söz konusu değişken fonksiyon öncesinde tanımlanmadıyısa global alanda bulamadığı için çağırma işlemi olmayacaktır.

# Bu konseptin geneline namespace (etki alanı) adı verilir. Bu durum sadece değişkenler için değil, fonksiyonlar için de geçerli bir durumdur.


# %%

# Python'da block (for, if, elif, else, while içerisine yazılan kodlar) scope mevcut değildir.
# Örneğin bir if bloğu içerisinde oluşturduğumuz değişkeni global etki alanında çağırabiliriz.
# Ancak fonksiyon içerisinde oluşturulan değişkeni global etki alanında çağıramayız.

secenek = 3
liste = [1, 2, 3]
if 5 > secenek:
    yeni_deger = liste[0] # if bloğu içerisinden yeni değişken oluşturuldu

print(yeni_deger) # söz konusu değişken çağrıldı.

# %%

# Tavsiye edilmeyen bir yöntem olup global etki alanındaki değişkene ait değerin lokal etki alanında
# güncellenmesini istediğimizde değişken isminin başına global anahtar kelimesi getirmemiz gerekebilir.

c = 10 # global değişken


def etki_c():
    global c  # global etkiye erişimi açık değişken oluşturuldu
    c += 1  # değer güncellendi.
    print(c)


etki_c()

# Genel kanıya göre global alanda oluşturulan değişkeni lokal alanda çağırın, kullanın ama yeniden düzenlemeyin.
# Çünkü istenmeyen mantıksal hatalara sebep olabilir.

# %%

# Eğer global alana etki etmek istiyorsak local alanda return ifadesini kullanabiliriz.
# Yukarıdaki örneği daha uygulanabilir hale getirelim.

c = 10  # global değişken


def etki_c():
    return c + 1  # global etki alanında bulunan değeri güncelledik


c = etki_c() # güncellenen değeri değişkene yeniden tanımladık
print(c)

# %%

# Global Sabitler

# Değiştirmeyi düşünmediğiniz global alanda oluşturacağınız sabit değerleri büyük harfler ile tanımlayın.
# Örneğin PI, URL, TWITTER_HANDLE gibi sabitler büyük harfle tanımlanabilir.

PI = 3.14  # bu değeri değiştirmemek üzere bir kere kullan.
URL = "https://www.cemalcici.com"
