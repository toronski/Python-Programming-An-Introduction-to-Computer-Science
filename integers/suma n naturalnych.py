# Program do obliczania sumy podanych n liczb naturalnych.

def main():
    print("Program do obliczania sumy 'n' liczb naturalnych.")

    n = eval(input("Podaj ile liczb naturalnych mam zsumować: "))
    razem = 0

    for i in range(1, n + 1):
        razem = razem + i

    print("Suma ", n, "liczb naturalnych daje ", razem, ".")

main()
