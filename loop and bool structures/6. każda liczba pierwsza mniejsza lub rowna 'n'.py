# 6. kazda liczba pierwsza mniejsza lub rowna 'n'.py

from math import *
import sys

def is_prime(num):
    is_prime = True
    for i in range(2, round(sqrt(num) + 1)):
        if num % i == 0:
            is_prime = False
            break
    return is_prime

def main():
    num = eval(input("Wpisz liczbę dodatnią: "))
    
    if num < 0:
        print("!!! BŁĄD !!!\n'n' powinno być liczbą dodatnią!")
    else:
        for i in range(2, num + 1):
            if is_prime(i):
                if i == 2:
                     print(2, end='')
                else:
                     print(',', i, end='')
        print()

main()
