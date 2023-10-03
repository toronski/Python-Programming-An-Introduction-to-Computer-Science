# ciąg Fibonacciego.py

def main():
    n = eval(input("Którą liczbę Fibonacciego program ma pokazać?"))

    prev = 1
    fib = 1
    for i in range(2, n):
        temp = prev
        prev = fib
        fib = temp + fib

    print("Wartość ", str(n), "liczby w ciągu Fibonacciego wynosi", fib)

main()
