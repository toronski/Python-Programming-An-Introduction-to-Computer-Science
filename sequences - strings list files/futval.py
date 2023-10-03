# futval.py

def main():
    print("\nProgram oblicza przyszłą wartość")
    print("dziesięcioletniej inwestycji.")

    principal = eval(input("Wpisz kwotę początkową: "))
    apr = eval(input("Wpisz roczny procent: "))
    years = eval(input("Ile lat będzie trwać inwestycja: "))

    print("\nYear   Value")
    print('-' * 16)

    for i in range(years):
        print("{0:>3}   {1:>5.2f}".format(i, principal))
        principal = principal * (1 + apr)

main()
