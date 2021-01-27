# %%

# Fonksiyonlarda Çıktı

# Fonksiyonların sonunda değer döndürmek için return kelimesi kullanılır.

# return kullanılmadan fonksiyon çalıştırma
def isim_formatlama(isim, soyisim):
    f_isim = isim.title()
    f_soyisim = soyisim.title()
    print(f"{f_isim} {f_soyisim}")

print(isim_formatlama("CeMaL", "cİcİ")) # ifade yazar ama None değeri döner
# %%

# return kullanılarak fonksiyon çalıştırma
# !!!!return kelimesinden sonra hiçbir komut çalışmaz!!!!
def isim_formatlama(isim, soyisim):
    f_isim = isim.title()
    f_soyisim = soyisim.title()
    return f"{f_isim} {f_soyisim}"
    print("İsim yazdırıldı ")

print(isim_formatlama("CeMaL", "cİcİ")) # sadece ifade yazar
# %%

def isim_formatlama(isim, soyisim):
    if isim == "" or soyisim == "":
        return "Hatalı değer girdiniz!"
    f_isim = isim.title()
    f_soyisim = soyisim.title()
    return f"{f_isim} {f_soyisim}"

print(isim_formatlama(input("İsminizi giriniz: "), input("Soyisminizi giriniz: "))) 

# Burada girilen isim bilgisi boş girilirse return ifadesi ile diğer komutların çalışması kesilmesi sağlanır.
# %%

# Docstrings

# Docstring yapısı program içerisinde basit anlamda dökümantasyon oluşturmayı sağlar.
# Python'da docstring yapısı, fonksiyon tanımlandıktan hemen sonra üç çift tırnak ile oluşturulur.

def isim_formatlama(isim, soyisim):
    """
    Dışarıdan alınan ismin olağan biçimde formatlanmasını sağlar.
    """
    if isim == "" or soyisim == "":
        return "Hatalı değer girdiniz!"
    f_isim = isim.title()
    f_soyisim = soyisim.title()
    return f"{f_isim} {f_soyisim}"

# Üç çift tırnak arasında çoklu yorum satırı oluşturulabilir ancak efektif değildir. 
# Bunun yerine her bir satırda # işlecininin kullanılması tavsiye edilir.