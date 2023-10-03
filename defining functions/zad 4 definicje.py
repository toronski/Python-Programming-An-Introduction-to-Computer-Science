# zad 4 definicje.py

def sumN(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

def sumNCubes(n):
    sum = 0
    for i in range(1, n+1):
        sum += i ** 3
    return sum

def main():
    n = eval(input("Wpisz liczbe naturalną: "))

    print("Suma pierwszych 'n' liczb naturalnych to ", sumN(n))
    print("Suma pierwszch 'n' podniesionych do sześcianu to ",  sumNCubes(n))

main()
