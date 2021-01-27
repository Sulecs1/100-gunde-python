# Arkadaşlarımız ile yemeğe çıktığımızı ve hesabı ortak ödemek istediğimizi düşünelim.
# Gelen yemek hesabı ile birlikte bahşişi de işin içine kattığımızda her birimizin ne kadar ödeme yapması gerektiğini bulalım.

# Karşılama mesajımızı yazdırıyoruz.
print("Welcome to the tip calculator.")

# Kullanıcıdan gerekli verileri alıyoruz
total_bill = float(input("What was the total bill? $"))
per_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
bill_split = int(input("How many people to split the bill? "))

# Örneğin $150 hesap olduğunu, hesabın 15%'i kadar bahşiş vermek istediğimizi ve 5 kişi yemek yediğimizi düşünelim.
# (150 / 5) * 1.15 = $34.5 kişi başı hesap düşer.
# Buradaki 1.15 değerini bulmak için de 1 + 15 / 100 hesabı ile buluruz.
# Yukarıda anlatılan matematiksel işlemi Python ile hesaplıyoruz.   
result = (total_bill / bill_split) * (1 + per_tip / 100)

# Sonucu ondalık basamağı 2 olacak şekilde ekrana yazdırıyoruz.
print(f"Each person should pay: ${round(result, 2)}")