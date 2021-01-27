# Bir rock grubu kurmak istediğimizi ve söz konusu bu grup için isim arayışında olduğumuzu düşünelim. 
# Bunun için kullanıcıya birtakım sorular soralım ve cevaplanan sorular ile rock grubumuzun ismini oluşturalım :).

# İlk önce karşılama mesajımızı yazıyoruz
print("Welcome to the Band Name Generator.")

# Kullanıcıdan gerekli verileri alıyoruz.
city_name = input("What's name of the city you grew up in?\n")
pet_name = input("What's your pet's name?\n")

# Alınan bilgileri birleştiriyoruz.
print("Your band name could be" + city_name + " " + pet_name)