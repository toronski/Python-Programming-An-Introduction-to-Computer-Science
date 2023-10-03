# Program do obliczania objętości i pola powierzchni sfery
# na podstawie promienia wpisanego przez użytkownika.

import math

def main():
    print("Ten program obliczy za ciebie objetość i pole powierzchni sfery na podstawie długości promienia.")
    r = float(input("Wpisz promień sfery: "))
    v = 4 / 3 * math.pi * r ** 3
    a = 4 * math.pi * r ** 2
    print("Sfera o promieniu ", r, "jednostek ma objętość ", v, " i pole powierzchni ", a,
          "tych jednostek.")
main()
