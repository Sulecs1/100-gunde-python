# Bugüne kadar yazdığımız program yöntemsel programlama tekniğine daylı idi.
# Yani iç içe geçmiş işlemşler, birbiri ile karışık bir şekilde bağlantı kurmuş nesneler mevcuttu.

# Daha karmaşık projelerde yöntemsel programlama kod ve çalışma karmaşıklığına sebep olabilir.

# OOP, büyük projeyi küçük parçalara bölmektir ve her bir parça üzerinde çalışacak sistem geliştiren yazılım geliştirme yöntemidir.

# Herhangi bir obje, neye sahip ve ne yapabilir sorularına cevap verebilir.
# Neye sahip olduğuna attributes(öznitelik), ne yapabildiğine ise method(metot) diyoruz.

# öznitelikler, program genelinde değil nesne özelinde barınırlar. Bu sayede programda daha az yer kaplarlar.
# metotlar ise program genelinde fonksiyonel olarak çağırılmazlar ve nesneye özgüdür.

# program içerisinde üretilen ve sürekli çağrılan nesnelere sınıf adı veriyorken, her bir sınıfa ait oluşturulan yapılara ise nesne diyoruz.
# Bu olaya sınıftan örnek nesne alma adı verilir.
# Biz, oluşturulan bir sınıftan istediğimiz kadar nesne üretebiliriz.


# from turtle import Turtle, Screen # başka bir kütüphane çağırdık.

#  nesne    sınıf
# timmy = Turtle()

# print(timmy) # nesneyi ekrana yazdıtıyoruz

#  nesne.metot()  --> basit anlamda nesneden metot çağırma.
# timmy.shape("turtle")
# timmy.color("green")
# timmy.forward(100)

# my_screen = Screen() # nesne oluşturduk

#        nesne.öznitelik --> basit anlamda nesneden öznitelik çağırma
# print(my_screen.canvheight)
# my_screen.exitonclick()

# Yukarıda nesne oluşturma, öznitelik ve metot çağırma işlemleri aşağıda da örnek olarak gösterilmiştir.

# from prettytable import PrettyTable
#
# table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = "l"
# print(table)
