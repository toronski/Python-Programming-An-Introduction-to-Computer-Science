# Program do obliczania sumy potęgi sześcianów podanych 'n' liczb naturalnych.

def main():
    print("Program do obliczania sumy potęgi sześcianów podanych 'n' liczb naturalnych.")

    n = eval(input("Ile liczba naturalnych do potęgi trzeciej mam zsumować: "))
    razem = 0

    for i in range(1, n+1):
        i = i ** 3
        razem = razem + i

    print("Suma ", n, "liczb(każdej podniesionej do szcześcianu) daje: ", razem)

main()

