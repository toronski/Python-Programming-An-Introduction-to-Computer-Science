
"""
def main():
    print("Ten program kalkuluję przyszłą wartość")
    print(" inwestycji.")

    principal = eval(input("Wpisz kwotę początkową: "))
    apr = eval(input("Wpisz roczne oprocentowanie: "))
    years = eval(input("Wpisz ile lat pieniądze będą na siebie zarabiać: "))
    for i in range(years):
        principal = principal * (1 + apr)

    print("Przez ", years, "lat zarobisz: ", principal)

main()
"""

"""
def main():
    principal = eval(input("Kwota inwestycji: "))
    apr = eval(input("Procent roczny: "))
    lata = eval(input("Na ile lat: "))
    coRoku = eval(input("Kwota wpłacana co roku: "))

    for i in range(lata):
        principal = principal + coRoku
        principal = principal * (1 + apr)
    print("Wartość inwestycji w", lata, "lat wyniesie:", principal)

main()
"""

def main():
    print("Ten program kalkuluje zysk z inwestycji")
    print("w oparciu o kwotę początkową, oprocentowanie roczne,")
    print("liczbę kapitalizacji odsetek w ciągu roku i liczbę lat inwestycji.")

    princ = eval(input("Pierwotna kwota inwestycji: "))
    apr = eval(input("Oprocentowanie w skali roku: "))
    kapit = eval(input("Liczba kapitalizacji odsetek w ciągu roku: "))
    lata = eval(input("Na ile lat: "))
    kaptRok = apr / kapit
    rocznie = lata * kapit
    
    for i in range(rocznie):
        princ = princ * (1 + kaptRok)

    print("Przez ", lata, " lat zarobisz ", princ, ".")

main()

