# wyniki quizu.py

def main():
    n = eval(input("Wpisz liczbę punktów(0-5): "))

    if n <= 1:
        grade = "F"
    elif n == 2:
        grade = "D"
    elif n == 3:
        grade = "C"
    elif n == 4:
        grade = "B"
    else:
        grade = "A"

    print("Twoja ocena to ", grade)

main()
