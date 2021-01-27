# Fiyat Teklifi Uygulaması

# Burada amaç gizli bir şekilde fiyat teklifi veren kişilerden en yüksek fiyatı veren kişiye ürünün satıldığının bilgisini ekrana yazdırmak.
import os
import art

def sozluge_kaydet(kisi_adi, teklif_ucreti):
    kisi_kaydi = {
        "ismi": kisi_adi,
        "ucret": teklif_ucreti
    }

    kisi_listesi.append(kisi_kaydi)

def en_buyuk_bul(kisiler):
    enB = 0
    kisi_ismi = ""

    for kisi in kisiler:
        if kisi["ucret"] > enB:
            enB = kisi["ucret"]
            kisi_ismi = kisi["ismi"]
    
    return enB, kisi_ismi

print(art.logo)

kisi_listesi = []
tekrar_sor = True

while tekrar_sor:
    isim = input("İsmin nedir?: ").title()
    teklif = int(input("Teklif ücreti nedir?: ₺"))
    sozluge_kaydet(kisi_adi=isim, teklif_ucreti=teklif)
    secenek = input("Başka teklif verecek var mı? 'evet' veya 'hayır' olarak belirt.").lower()
    if secenek == "hayır":
        tekrar_sor = False
    os.system("cls")

print(f"Kazanan {en_buyuk_bul(kisiler=kisi_listesi)[1]}! Verdiği teklif ücreti {en_buyuk_bul(kisiler=kisi_listesi)[0]}₺.")
