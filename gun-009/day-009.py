# %% 

# Sözlükler

# Python'da sözlükler sözlüğe benzer.
# {anahtar: değer} şeklinde tanımlanır.
# {anahtar1: değer1, anahtar2: değer2} şeklinde birden fazla kez yazılabilir.

# Tek değerli bir sözlük oluşturma
rehber = {"isim": "Cemal"}
print(rehber)

# Birden fazla değerli sözlük oluşturma
rehber = {
    "isim": "Cemal",
    "soyisim": "Cici",
    "yaşadığı yer": "Trabzon"
}
print(rehber)

# Sözlük değerini yazdırma
print(rehber["soyisim"])

# Sözlüğe yeni değer ekleme
rehber["yaş"] = 25
print(rehber)

# Sözlük değerini değiştirme
rehber["yaşadığı yer"] = "Ankara"
print(rehber)

# Döngü ile bütün değerleri yazdırma
for anahtar in rehber:
    print(anahtar)
    print(rehber[anahtar])
# %%

# İç İçe Sözlükler

baskentler = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Sözlük içinde liste

gezi_kayit = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Sözlük içinde sözlük

gezi_kayit = {
    "France": {"gezilen_sehirler": ["Paris", "Lille", "Dijon"], "toplam_ziyaret": 12},
    "Germany": {"gezilen_sehirler": ["Berlin", "Hamburg", "Stuttgart"], "toplam_ziyaret": 5},
}

# Liste içinde sözlük

gezi_kayit = [
{
    "sehir": "France", 
    "gezilen_sehirler": ["Paris", "Lille", "Dijon"], 
    "toplam_ziyaret": 12,
},
{
    "sehir": "Germany",
    "gezilen_sehirler": ["Berlin", "Hamburg", "Stuttgart"],
    "toplam_ziyaret": 5,
},
]
