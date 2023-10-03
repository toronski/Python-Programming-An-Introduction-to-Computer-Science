# Program do obliczania wymaganej długości drabiny, aby dosięgnąć czegoś wysoko.

import math

def main():
    print("Jak długa musi być drabina, aby dosięgnąć na określoną odległość?")
    print("Sprawdźmy!")

    angle = eval(input("Pod jakim kątem ma stać drabina: "))
    wysokosc = eval(input("Wysokość na jaką chcemy dosięgnąć: "))

    radians = (math.pi / 180) * angle
    dlugosc_drabiny = wysokosc / (math.sin(radians))

    print("Drabina musi mieć długość: ", round(dlugosc_drabiny, 3), "jednostek.")

main()

