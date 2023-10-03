# Program do obliczania dystansy pomiędzy dwoma punktami.

import math

def main():
    print("Program obliczający dystans pomiędzy dwoma punktami.")

    x1 = eval(input("Współrzędne x1: "))
    y1 = eval(input("Współrzędne y1: "))
    x2 = eval(input("Współrzędne x2: "))
    y2 = eval(input("Współrzędne y2: "))

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    print("Dystans pomiędzy podanymi punktami wynosi: ", round(distance, 3), "jednostek.")

main()
