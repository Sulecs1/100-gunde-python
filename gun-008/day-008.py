# %%

## Fonksiyonların Değer Alması

# Review: 
# Create a function called greet(). 
# Write 2 print statements inside the function.
# Call the greet() function and run your code.

def greet():
    print("Hello")
    print("How do you do?")

greet()
# %%

def greet_with_input(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet_with_input("Cemal")

# Basit anlamda fonksiyonlar parantez içerisinde bir şey olmadan çalışabilirler.
# Aynı şekilde içerisine veri eklendiğinde de çalışabilirler.
# Burada name isimli değişkene parametre, "Cemal" isimli değere de argüman adı veririz.
# Fonksiyonlar parametreler sayesinde argüman alabilirler.

# %% 

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("Cemal", "Ankara")

# Burada dikkat edilmesi gereken nokta parametrelere verilen argüman değerlerinin sırayla veriliyor olması. 
# Bu duruma sıralı argüman tanımı deniniyor. Sıralı parametrelere farklı sıralarda argüman verilirse hata olabilme ihtimali yükselir.
# Bu durumda anahtar kelimeli argüman tanımı geliyor.

greet_with(location="Ankara", name="Cemal")

# Anahtar kelimeli argümanda parametre isminin yazılması gerekiyor. Bu sayede hangi sırada yazılsın argümanlar doğru parametreleri bulabiliyor.