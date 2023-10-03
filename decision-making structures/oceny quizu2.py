# oceny quizu2.py

def main():
    n = eval(input("Wpisz ilość punktów(0-100): "))

    if 100 >= n >= 0:
        if n < 60:
            grade = "F"
        elif 69 >= n >= 60:
            grade = "D"
        elif 79 >= n >= 70:
            grade = "C"
        elif 89 >= n >= 80:
            grade = "B"
        else:
            grade = "A"

        print("Twoja ocena to ", grade)
        
    else:
        print("Błąd - zły wynik punktowy.")

main()
