# Program do obliczania ceny za 1 cm2 pizzy
# w oparciu o jej wielkość i cenę.

import math

def main():
    print("Kalkulator ceny za 1 cm2 pizzy w oparciu o jej wielkość i cenę.")
    
    diemeter = input("Podaj wielkość pizzy: ")
    price = input("Podaj cenę  tej pizzy: ")
    radius = int(diemeter) // 2
    pole = math.pi * radius
    priceCm2 = int(price) / pole

    print("Cena za 1cm2 pizzy kosztującej ", price, " o wielkości ", diemeter,
          " wyniesie: ", round(priceCm2, 2), "złotych.")

main()
