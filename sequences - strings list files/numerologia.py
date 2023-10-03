# numerologia.py

# Numerolodzy twierdzą, że są wstanie określić czyjeś cechy na podstawie
# "numerycznych wartości" imienia. Wartość imienia determinuje się
# poprzez przywołanie wartości liter imienia, gdzie 'a' to 1, 'b' to 2,
# 'c' to 3, aż do 'z' to 26.
# Imię 'Zelle' ma wartości 26 +5 +12 + 12 + 5 = 60.
# Napisz program, który oblicza numeryczną wartość imienia wpisanego
# przez użytkownika.

def main():
    print("Program oblicze wartość numeryczną wpisanego imienia")
    name = input("Wpisz imię: ").lower()

    litery = " abcdefghijklmnopqrstuvwxyz"
    
    wartosc = 0
    for i in name:
            wartosc = litery.find(i) + wartosc

    print("Wartość numeryczna podanego imienia to: ", wartosc)

main()
        
