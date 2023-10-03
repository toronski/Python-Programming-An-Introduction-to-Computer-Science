# numerologia2.py

# program rozwiniety o sprawdzanie wartosci calego imienia i nazwiska

def main():
    print("Program oblicze wartość numeryczną wpisanego imienia")
    name = input("Wpisz pełne imię i nazwisko(bez polskich znaków): ").lower()
    

    litery = " abcdefghijklmnopqrstuvwxyz"
    wartosc = 0
    for i in name:
        print(i, litery.find(i))  
        wartosc = litery.find(i) + wartosc

    print("Wartość numeryczna podanego imienia to: ", wartosc)
    
main()
