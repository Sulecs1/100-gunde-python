# Program ihtiyaç analizi: Programlamada müşterinin ihtiyacını belirlemek, programı oluşturmak için önemli konulardan birisidir.
# Aşağıdaki listede müşteri eğitmenin ihitiyaç raporundan özet çıkardım. Aşağıdaki şekilde hazır olmasını istediği bir program var.

# TODO: + 1. Hangi kahve çeşidiini istediğini sor.
# TODO: + 1.1. Kullanıcının girdisine göre ne yapacağına karar ver.
# TODO: + 1.2. Seçimden sonra işlemler tamamlandığında tekrar bu soruyu sor.
# TODO: + 2. "kapat" komutu girildiğinde programı sonlandır.
# TODO: + 3. rapor sistemi oluştur.
# TODO: + 3.1. "rapor" yazıldığında aşağıdaki gibi bir çıktı versin.
# Su: 100ml
# Süt: 50ml
# Kahve: 76g
# Para: 2.5₺
# TODO: + 4. Elindeki kaynakları kontrol et.
# TODO: + 4.1. Bir içecek seçildiğinde içecek oluşturmak için gereken malzemenin kaynaklarında olup olmadığını sorgula.
# TODO: + 4.2. Eğer elindeki kaynaklar yetmiyor ise "Üzgünüm elimde ... kalmadı." şeklinde bir ifade ile birinciyi maddeye dön.
# TODO: + 5. İlk dört aşama tamamlandıktan sonra para alma işlemine geç.
# TODO: + 5.1. Eğer girilen ücret seçilen kahvenin ücretinden az ise "yetersiz bakiye" diye belirt ve birinci maddeye dön.
# TODO: + 5.2. Eğer girilen ücret seçilen kahvenin ücretinden fazla ise para üstünü hesapla ve geri verdiğini işaret eden mesaj ver.
# TODO: + 5.3. Para için sadece bozuk paralar geçerli. 5Kr, 10kr, 25kr, 50kr ve 1₺ olacak şekilde para değerlerini iste.
# TODO: + 6. Eğer işlem başarılı bir şekilde gerçekleştiyse buna göre eldeki kaynakları güncelle.
# TODO: + 6.1. Aşağıda basit bir örnek verdim.
# Latte yapmadan önceki kaynaklarımız.
# Su: 300ml
# Süt: 200ml
# Kahve: 100g
# Para: 0₺
# Latte yapıldıktan sonraki kaynaklarımız.
# Su: 100ml
# Süt: 50ml
# Kahve: 76g
# Para: 2.5₺

### KODLAMA ###

MENU = {
    "espresso": {
        "malzemeler": {
            "su": 50,
            "kahve": 18,
        },
        "fiyat": 1.5,
    },
    "latte": {
        "malzemeler": {
            "su": 200,
            "süt": 150,
            "kahve": 24,
        },
        "fiyat": 2.5,
    },
    "cappuccino": {
        "malzemeler": {
            "su": 250,
            "süt": 100,
            "kahve": 24,
        },
        "fiyat": 3.0,
    }
}

BOZUKLUK = {
    "5 Kuruş": 0.05,
    "10 Kuruş": 0.10,
    "25 Kuruş": 0.25,
    "50 Kuruş": 0.50,
    "1 TL": 1.0
}

kaynaklar = {
    "su": 300,
    "süt": 200,
    "kahve": 100,
}

def kaynaklar_yeterli_mi(kahve_turu:str):
    yeterli = True
    eksik_malzemeler = []
    for malz in MENU[kahve_turu]["malzemeler"].keys():
        if not kaynaklar[malz] >= MENU[kahve_turu]["malzemeler"][malz]:
            yeterli = False
            eksik_malzemeler.append(malz)
    return yeterli, tuple(eksik_malzemeler)

def stok_dus(kahve_turu:str):
    for malz in MENU[kahve_turu]["malzemeler"].keys():
        kaynaklar[malz] -= MENU[kahve_turu]["malzemeler"][malz]

def bozuk_para_haznesi():
    BOZUKLUK = {
        "5 Kuruş": 0.05,
        "10 Kuruş": 0.10,
        "25 Kuruş": 0.25,
        "50 Kuruş": 0.50,
        "1 TL": 1.0
    }
    toplam_para = 0
    for bozuk_turu in BOZUKLUK.keys():
        para = int(input(f"Kaç adet {bozuk_turu} var: "))
        toplam_para += BOZUKLUK[bozuk_turu] * para
    return toplam_para


def siparis(kahve_turu:str):
    if kaynaklar_yeterli_mi(kahve_turu)[0]:
        odenen_ucret = bozuk_para_haznesi()
        if odenen_ucret < MENU[kahve_turu]["fiyat"]:
            print("Bakiyen yetersiz.")
        else:
            print(f"İstediğin {kahve_turu.title()} hazır! Afiyet olsun!")
            print(f"Para üstün toplamda {round((odenen_ucret - MENU[kahve_turu]['fiyat']), 2)}₺. Geri almayı unutma!")
    else:
        print(f"Üzgünüm. Elimdeki bazı malzemeler bitti. {kaynaklar_yeterli_mi(kahve_turu)[1]} ")

kapandi_mi = False
bakiye = 0.0

while not kapandi_mi:
    secenek = input("Hangi kahve çeşidini istiyorsun? (espresso/latte/cappuccino)").lower()
    if secenek == "kapat":
        kapandi_mi = True
    elif secenek == "rapor":
        print(f"Su: {kaynaklar['su']}\nSüt: {kaynaklar['süt']}\nKahve: {kaynaklar['kahve']}\nPara: {bakiye}₺")
    elif secenek == "espresso" or secenek == "latte" or secenek == "cappuccino":
        siparis(secenek)
        bakiye += MENU[secenek]['fiyat']
        stok_dus(secenek)
    else:
        print("Hatalı seçim yaptınız!\n")
