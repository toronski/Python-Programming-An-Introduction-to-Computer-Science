# oceny 2.py

def ocena(wynik):
    oceny = 60 * "F" + 10 * "D" + 10 * "C" + 10 * "B" + 11 * "A"
    return oceny[wynik]

def main():
    print("Program wylicza oceny na podstawie punktacji")

    wynik = eval(input("Wpisz liczbę punktów(od 0 do 100): "))

    print("Ocena to ", ocena(wynik))

main()

