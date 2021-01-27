### Kendi Nesnemizi Oluşturma ###

class User:  # sınıf oluşturmak için class anahtar kelimesi kullanılır.
    # __init__ fonksiyonu sınıftan her bir nesne oluştuğundaki oluşturulacak değişkenleri tutar.
    def __init__(self, user_id, username):
        # self anahtar kelimesi sınıfa ait her bir nesne oluşturucusu olarak tanımlanabilir.
        self.id = user_id  # nesne oluşturulurken kullanıcıdan alınan değer, her bir oluşturu için yeni özniteliğe atanır.
        self.username = username  # kullanıcıdan alınan parametre ismi ile sınıftaki öznitelik ismi aynı olabilir.
        self.followers = 0  # bazı öznitelikler kullanıcıdan değer alınmadan oluşabilirler.
        self.following = 0

    def follow(self, user):
        # Sınıflarda metotlar tanımlanırken self parametresi otomatik olarak ilk sırada yer alır.
        # Bunun anlamı, bu metot ne zaman çağrılır ise nesne bu fonksiyonu çağırmış demektir.
        user.followers += 1  # takip edilecek kullanıcı girildiğinde kullanıcının takipçisi bir artar
        self.following += 1  # takip eden kullanıcının takip ettiği değer bir artar

user_1 = User("001", "cemal")
user_2 = User("002", "cesur")

user_1.follow(user_2)
print(user_1.followers)  # 0
print(user_1.following)  # 1
print(user_2.followers)  # 1
print(user_2.following)  # 0
