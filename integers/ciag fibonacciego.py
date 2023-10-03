# Program wyrzucający liczbę fibonnaciego o określonym miejscu.

def main():
    n = eval(input("Wpisz, którą liczbę z ciągu Fibonacciego mam pokazać: "))
    fib = [0, 1]

    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])

    fib_Num = fib[n]
    
    print(n, "liczba w ciągu Fibonacciego to:", fib_Num)

main()
