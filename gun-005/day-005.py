# %%

## Döngüler

# Programlamada bazı işlemler tekrar tekrar gerçekleşebilir. Bunun için de döngüler kullanılır.
# Python'da kullanılan dönglerden biri de for döngüsüdür.

fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)

# 
# %%

## range() fonksiyonu

# For döngüsü her zaman listeler ile kullanılamayabilir. Bazı durumlarda iteratif işler de gerçekleştirmek istenebilir ve range() fonksiyonu bu işlemi sağlar.

for number in range(1, 11): # 1 dahil 11 dahil değil.
    print(number)

# %%

# ilk parametresi başlangıç değeri, ikinci parametresi bitiş değeri (dahil değil), üçüncü parametresi ise adım sayısı olarak kullanılır.

for number in range(1, 11, 3):
    print(number)

# %%

# 1-100 değerlerinin toplamını bulan program

total = 0
for number in range(1, 101):
    total += number
print(total)