# Fibonacci z funkcja
# Program wyrzucający liczbę fibonnaciego o określonym miejscu.

def fibo(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib


def main():
    n = eval(input("Write with number from Fibonacci sequencu you want to see: "))

    fib_Num = fibo(n)
    
    print(n, "number in fibonacci sequence is:", fib_Num[n])

main()
