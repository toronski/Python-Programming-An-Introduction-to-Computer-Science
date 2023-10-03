# Program do obliczania zarobku z lokaty
'''
def main():
    print("Program do obliczania zarobkub z lokaty")
    K = eval(input("Podaj zdeponowaną kwotę: "))
    p = eval(input("Podaj procent w skali roku: "))
    k = eval(input("Co ile (w miesiącach) naliczają się odsetki: "))
    n = eval(input("Jak długo pieniądze będą na siebie zarabiać: "))
    c = 20
    kapt = 12 / k
    wynik = K * (1 + (p*(1 - (c/100)) / 100 * kapt)) ** kapt*n

    print("W przeciągu " + str(n) + " lat, przy oprocentowaniu " + str(p) + "% zarobisz: "
          + str(wynik) + ".")
main()

'''

def book():
    inwestycja = eval(input("Początkowa inwestycja: "))
    rate = eval(input("Roczne oprocentowanie: "))
    period = eval(input("Co ile następuje kapitalizacja: "))
    lata = eval(input("Na ile lat zainwestujesz: "))

    for i in range(lata):
        inwestycja = inwestycja * (1 + rate/period)

    print("W ciągu 10 lat kwota inwestycji wyniesie:", inwestycja)

book()

