# maxn.py

def main():
    n = int(input("Jak dużo mamy numerów? "))

    maxval = float(input("Wpisz numer >> "))

    for i in range(n-1):
        x = float(input("Wpisz numer >> "))
        if x > maxval:
            maxval = x



    print("Największa wartość wynosi ", maxval)

main()
