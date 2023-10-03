# rząd US.py

def main():
    age = eval(input("Wiek: "))
    citizenship = eval(input("Lata obywatelstwa: "))

    if age >= 30:
        if citizenship >= 9:
            print("Senat stoi otworem.")
            if citizenship >= 7:
                print("Izba reprezentantów stoi otworem.")
        elif citizenship >= 7:
            print("Izba reprezentantów stoi otworem.")
        else:
            print("Panie Areczku, bycie w rządzie jest dla"\
                  " obywateli\nz dłuższym starzem obywatelstwa.")

    elif age >= 25:
        if citizenship >= 7:
            print("Izba reprezentantów stoi otworem.")
        else:
            print("Panie Areczku, bycie w rządzie jest dla"\
                  " obywateli\nz dłuższym starzem obywatelstwa.")
    else:
        print("Panie Areczku, bycie w rządzie jest dla starszych.")
        
main()
