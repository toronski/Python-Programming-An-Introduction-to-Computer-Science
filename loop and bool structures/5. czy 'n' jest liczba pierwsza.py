# 5. czy 'n' jest liczbą pierwsza.py

from math import *
import sys

def main():
    n = eval(input("Wpisz liczbę dodatnią większą od 2: "))

    if n < 2:
        print("!!! BŁĄD !!!\n'n' powinno być większe od '2'!")
    elif n < 0:
        print("!!! BŁĄD !!!\n'n' powinno być liczbą dodatnią!")
    else:
        for i in range(2, round(sqrt(n) + 1)):
            if n % i == 0:
                print("\'n' nie jest liczbą pierwszą.")
                print("Program kończy działanie.")
                sys.exit()
        print("\'n' jest liczbą pierwszą.")

main()
