# Program do obliczania pola trójkąta.

import math

def main():
    print("To program do obliczania pola trójkąta.")
    a = eval(input("Bok A: "))
    b = eval(input("Bok B: "))
    c = eval(input("Bok C: "))

    s = (a+b+c)/2
    A = math.sqrt(s * ((s-a) * (s-b) * (s-c)))

    print("Pole trójkąta wynosi: ", round(A, 3), "jednostek.")

main()

