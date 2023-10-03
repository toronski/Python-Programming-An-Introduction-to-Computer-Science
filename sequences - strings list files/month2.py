# month2.py

def main():

    # miesiaca jako lista w tabeli podgladowej
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep",
              "Oct", "Nov", "Dec"]

    n = eval(input('Wpisz numer miesiąca (1-12): '))

    print("Skrót miesiąca to ", months[n-1] + '.')

main()
