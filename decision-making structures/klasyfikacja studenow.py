# klasyfikacj studentow.py

def main():
    credits = eval(input("Wpisz liczbę zdobytych kredytów: "))

    if credits >= 26:
        student = "Senior"
    elif credits >= 16:
        student = "Junior"
    elif credits >= 7:
        student = "Sophomore"
    else:
        student = "Freshman"

    print("Twoja klasyfikacja to: ", student)

main()
