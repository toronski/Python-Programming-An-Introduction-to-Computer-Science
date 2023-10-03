# Program do obliczania ceny za 1 cm2 pizzy
# w oparciu o jej wielkość i cenę,
# używając FUNKCJI

import math

def pole(radius):
    return math.pi * radius

def priceCm2(pole, price):
    return int(price) / int(pole)

def main():
    print("Kalkulator ceny za 1 cm2 pizzy w oparciu o jej wielkość i cenę.")
    
    diemeter = input("Podaj wielkość pizzy: ")
    price = input("Podaj cenę  tej pizzy: ")
    radius = int(diemeter) // 2
    pole_pizzy = pole(radius)
    cena_kawalka = priceCm2(pole_pizzy, price)
    
    print("Cena za 1cm2 pizzy kosztującej ", price, " o polu ", pole_pizzy,
          " wyniesie: ", round(cena_kawalka, 2), "złotych.")

main()
