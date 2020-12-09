# %%

## Fonksiyonlar

# Tekrarlı işlemleri bir kez yazmak için kullanılan işlevlerdir.

# Fonksiyon tanımlama
def my_function():
    print("Hello") # gömülü fonksiyon
    print("Bye") # gömülü fonksiyon

# Fonksiyon Çağırma
my_function() # oluşturulan fonksiyon

# %%

## Girintiler

# Python'da kod blokları oluşturmak için girintiler kullanılır.

def say_hello():
    print("Hello") # girinti kullanılarak fonksiyon içerisinde kaldı
print("World") # girinti kullanılmadığı için fonksiyon dışında

# %%

# Girintiler herbir blok için oluşturulmalıdır.

def say_hello():
    sky = "clear" # say_hello fonksiyonunun içinde
    if sky == "clear":
        print("blue") # if kod bloğunun içinde
    elif sky == "cloud":
        print("gray") # elif kod bloğunun içinde
    print("Hello") # say_hello fonksiyonunun içinde
print("World") # fonksiyon dışında

# %%

## While Döngüsü

# For döngüsü iterasyon mantığı ile adım adım çalışmakta iken while döngüsü şarta bağlı olarak çalışmaktadır.

sayac = 6
while sayac > 0: # sayaç değeri 0'dan büyük olduğu sürece
    print(sayac) # sayaç değerini ekrana yazdır.
    sayac -= 1 # sayaç değerini bir azalt.

# For döngüsünü sayılabilen nesneler üzerinde ve sayma işleminde kullanılırken
# While döngüsü şarta bağlı tekrar yapılarında kullanılır.

# %%

# While döngüsünde sonsuz döngüye yakalanabiliriz. Bunun sebebi şartın sürekli doğru olmasından kaynaklıdır. Yukarıdaki örnekte sayac -= 1 ifadesini kaldırdığımızda ve çalıştırdığımızda döngü sonsuz döngüye girer.

sayac = 6
while sayac > 0:
    print(sayac)

# Bu sonsuz döngü bilgisayarın hafızasını şişerene kadar devam eder ve hafızanın yetmediği yerde durur.