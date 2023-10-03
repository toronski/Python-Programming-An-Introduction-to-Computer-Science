# username.py

# Prosty program przetwarzający do generowania nazw użytkownika.

def main():
    print("Ten program generuje nazwy używkonika. \n")

    # wez imie i nazwisko uzytkownika
    first = input("Proszę wpisać swoje imię małymi literami: ")
    last = input("Proszę wpisać swoje nazwisko małymi lliterami: ")

    # dodaj inicjal imienia do 7 znakow nazwiska
    uname = first[0] + last[:7]

    # wydaj naze uzytkownika
    print("Twoja nazwa użytkownika to: ", uname)

main()

