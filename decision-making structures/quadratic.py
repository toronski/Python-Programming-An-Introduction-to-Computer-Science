# quadratic.py

import math

def main():
    a = float(input("Podaj współczynnik A: "))
    b = float(input("Podaj współczynnik B: "))
    c = float(input("Podaj współczynnik C: "))

    discrim = b * b - 4 * a * c
    if discrim < 0:
        print("Równianie nie ma rzeczywistych pierwiastków!")
    elif discrim == 0:
        root = -b / (2 * a)
        print("Istnieje podwójny pierwiastek w", root)
    else:
        discRoot = math.sqrt(discrim)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print("\nWyniki to:", root1, root2)

main()
