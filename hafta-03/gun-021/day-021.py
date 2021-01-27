# Miras ALma (Inheritance)

class Animal:
    """
    Hayvanları temsilen bir sınıf tanımlandı
    """
    def __init__(self):
        self.num_eyes = 2  # göz sayısı

    def breathe(self):
        """
        Nefes alma fonksiyonu oluşturuldu
        :return:
        """
        print("Inhale, exhale.")


class Fish(Animal):  # Hayvan sınıfından miras alma işlemi
    def __init__(self):
        super().__init__()  # hayvan sınıfında bulunan bütün sınıf özellikleri getirildi

    def breathe(self):
        super().breathe()  # hayvan sınıfında bulunan nefes alma fonksiyonu çağrıldı
        print("doing this underwater.")  # çağrılan fonksiyona ilave işlemler yapıldı

    def swim(self):
        """
        Yümze fonksiyonu oluşturuldu.
        :return:
        """
        print("moving in water.")

nemo = Fish()
nemo.breathe()
