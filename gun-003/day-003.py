#%%

## Karşılaştırmalar
# Karşılaştırmalar hayatın her yerinde olduğu gibi programlama dünyasında da mecvutlar.
# Program akışı içerisinde şarta bağlı olarak akışı değiştirmek için karşılaştırma yapısı kullanılır.
# Python'da karşılaştırma yapıları if/else anahtar kelimeleri ile sağlanır.

## if-else
# Eğer/Değilse anlamı taşımakla beraber en temel karşılaştırma yapısıdır.
# Örneğin bir lunaparkta hız tireni bileti sattığınızı düşünelim. Hız trenine binmenin şartı ise binecek kişinin 120 cm'den uzun olması olsun. Python'da bu şartı aşağıdaki şekilde oluşturabiliriz.

print("Hız trenine hoş geldiniz!") # karşılama mesajı
boy = int(input("Cm cinsinden boy uzunluğun nedir? ")) # kullanıcıdan veri alındı

if boy >= 120: # eğer boy uzunluğu 120'den büyük ise
    print("Hız trenine binebilirsin.") # verilecek mesaj
else: # boy uzunluğu 120'den büyük değil ise
    print("Üzgünüm hız trenine binemezsin. Biraz boyun uzadıktan sonra yeniden gel.") # verilecek mesaj

# 15. satır incelendiğinde if anahtar kelimesi ile şart ifademizi belirtiyoruz.
# Söz konusu bu şart doğru olduğunda bir alt bloktaki işlem veya işlemleri gerçekleştiriyoruz.
# 17. satır incelendiğinde 15. satırda belirtilen şart doğru olmadığı durumda çalışmaktadır.

# Python indentation (girinti) mantığı ile çalışır. Girintiler : karakteri ile tanımlanır ve bir alt satırın 4 boşluktan (1 tab boşluğu) başlamasını sağlar. : karakterini temsil ediyordur.
# Buna göre 16. satır if boy > 120 ifadesini, 18. satır ise else ifadesini temsil etmektedir.

#%%

## Karşılaştırma Operatörleri

# >  --> Büyüktür
# <  --> Küçüktür
# >= --> Büyük veya eşittir
# <= --> Küçük veya eşittir
# == --> Eşittir
# != --> Eşit değildir

#%%

# İç içe karşılaştırma ve elif şartı oluşturma
# Bir önceki örneği detaylandıralım. Kişinin 120 cm'den uzun olduğu durumda:
# Eğer yaşı 12'den küçük ise 5₺, 12-18 yaş arasında ise 7₺ ve 18 yaşından büyük ise 12₺ ödemesi gerektiğini belirten programı yazalım.

print("Hız trenine hoş geldiniz!") 
boy = int(input("Cm cinsinden boy uzunluğun nedir? "))
if boy >= 120:
    print("Hız trenine binebilirsin.")
    yas = int(input("Lütfen yaşınızı giriniz: ")) # kullanıcıdan veri alındı
    if yas < 12: # eğer yaşı 12'den küçük ise
        print("Bilet ücretiniz 5₺.") # 5₺ ödemesi gerektiğini belirt.
    elif yas <= 18: # eğer yaşı 12-18 yaşları arasında ise
        print("Bilet ücretiniz 7₺.") # 7₺ ödemesi gerektiğini belirt.
    else: # yukarıdaki şartlardan hiçbiri değil ise
        print("Bilet ücretiniz 12₺.") # 12₺ ödemesi gerektiğini belirt.
else:
    print("Üzgünüm hız trenine binemezsin. Biraz boyun uzadıktan sonra yeniden gel.") 

# Python'de iç içe şartlar oluşturulabilir. Buradaki örnekte ödenecek bilet parasını belirtmek için birden fazla yaş seçeneğini karar yapısı olarak sorgulayabiliyoruz.
# if-else yapısında şartımız bir tane olmasıyla beraber birden fazla şartın olduğu karşılaştırmalarda if-elif-else yapısı kullanılır. else hiç değilse anlamını taşır ve if ile else ifadeleri arasında birden fazla else ifadesi gelebilir.

# %%

## Çoku Karşılaştırmalar

# Program akışı içerisinde birden fazla karşılaştırma işlemleri yapılabilir. Her bir if-else yapısı alınan karşılaştırmalar 1 karşılaştırma olarak yazılabilir.
# Örneğimize devam edelim ve kişi 3₺'lik ek ücret karşılığında hız trenindeyken fotoğraf çektirmek isteyip istemediğini soran karşılaştırmayı oluşturalım.

print("Hız trenine hoş geldiniz!") 
boy = int(input("Cm cinsinden boy uzunluğun nedir? "))
hesap = 0 # toplam hesap değeri oluşturuldu.
if boy >= 120:
    print("Hız trenine binebilirsin.")
    yas = int(input("Lütfen yaşınızı giriniz: "))
    
    # Karşılaştırma yapısı 1
    if yas < 12:
        hesap = 5
        print("Çocuk bileti 5₺.")
    elif yas <= 18:
        hesap = 7
        print("Öğrenci bileti 7₺.")
    else:
        hesap = 12
        print("Yetişkin bileti 12₺.")
    
    foto_istegi = input("Hız treninde bulunduğunuz anı oluşturmak ister misiniz? E. veya H.") # kullanıcıdan veri alındı
    
    # Karşılaştırma yapısı 2
    if foto_istegi == "E": # eğer cevap evet ise 3₺ ekle
        hesap += 3 # hesap = hesap + 3 (Unutmayın! Önce işlem, sonra atama)

    print(f"Toplam hesabınız {hesap}₺ olarak belirlendi.") # toplam hesap yazdırıldı
else:
    print("Üzgünüm hız trenine binemezsin. Biraz boyun uzadıktan sonra yeniden gel.")

# Bu programda iki adet karşılaştırma yapısı kuruluyor olup 1. karşılaştırma yapısı çağrıldıktan sonra 2. karşılaştırma yapısı çağrılmaktadır. Bu çözüm problemimize yönelik çözümdür.

#%%

## Mantıksal Operatör

# Bir karar yapısı İÇERİSİNDE birden fazla ŞART olabilir.
# Örneğimize devam edelim ve 45-55 yaş arasında olan kişilere bilet ücretinin alınmadığı özel bir günde olduğumuzu varsayarak toplam hesabı yeniden oluşturalım.

print("Hız trenine hoş geldiniz!") 
boy = int(input("Cm cinsinden boy uzunluğun nedir? "))
hesap = 0
if boy >= 120:
    print("Hız trenine binebilirsin.")
    yas = int(input("Lütfen yaşınızı giriniz: "))
    if yas < 12:
        hesap = 5
        print("Çocuk bileti 5₺.")
    elif yas <= 18:
        hesap = 7
        print("Öğrenci bileti 7₺.")
    elif yas >= 45 and yas <= 55: # 45-55 yaş arasında ise ücretsiz!
        print("Bugün özel bir gün! Sizlere bilet ücreti yok!")
    else:
        hesap = 12
        print("Yetişkin bileti 12₺.")
    
    foto_istegi = input("Hız treninde bulunduğunuz anı oluşturmak ister misiniz? E. veya H.")

    if foto_istegi == "E": 
        hesap += 3

    print(f"Toplam hesabınız {hesap}₺ olarak belirlendi.") # toplam hesap yazdırıldı
else:
    print("Üzgünüm hız trenine binemezsin. Biraz boyun uzadıktan sonra yeniden gel.")

# 117. satır incelendiğinde birden fazla şart ile oluşturulan bir karşılaştırma işlemi görülmektedir. Python'da birden fazla şart ile karşılaştırma ifadesi oluşturmak için mantıksal operatörler kullanılır.

# and --> ve    --> İki değeri "doğru" olduğu durumda "doğru", diğer durumlarda "yanlış" değerine sahip olmayı sağlayan operatördür.
# or  --> veya  --> İki değeri "yanlış" olduğu durumda "yanlış", diğer durumlarda "doğru" değerine sahip olmayı sağlayan operatördür.
# not --> değil --> "Doğru" değerin "yanlış", "yanlış" olan değerin "doğru" değerine sahip olmayı sağlayan operatördür.
