# lata przestepne.py
'''
def main():
    print("Sprawdź czy dany rok jeste przestępny")
    year = int(input("Podaj rok do sprawdzenia: "))

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Rok jest przestępny.")
            else:
                print("Rok nie jest przestępny.")
        else:
            print("Rok jest przestępny.")

    else:
        print("Rok nie jest przestępny.")

main()

'''

def main():
    year = int(input("Podaj rok do sprawdzenia: "))

    is_leap = False

    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            is_leap - True

    if is_leap:
        print(year, "jest rokiem przestępnym.")
    else:
        print(year, "nie jest rokiem przestępnym.")

main()
