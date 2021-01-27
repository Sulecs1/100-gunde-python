from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

para_makinesi = MoneyMachine()
kahve_makinesi = CoffeeMaker()
mak_menu = Menu()


acik_mi = True

while is_on:
    secenekler = menu.get_items()
    secenek = input(f"Hangi kahveden istiyorsun? {secenekler}: ")
    if senecek == "kapat":
        is_on = False
    elif senecek == "rapor":
        kahve_makinesi.report()
        para_makinesi.report()
    else:
        icecek_turu = menu.find_drink(secenek)
       if kahve_makinesi.is_resource_sufficient(icecek_turu) and  para_makinesi.make_payment(icecek_turu.cost):
           kahve_makinesi.make_coffee(icecek_turu)
