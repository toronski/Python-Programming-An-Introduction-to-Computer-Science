# inwestycja rosnąca co roku.py

def main():
    procent = eval(input("Podaj roczne oprocentowanie inwestycji: "))
    initial_Cash = eval(input("Podaj początkową kwotę inwestycji: "))

    total = initial_Cash
    years = 0

    while total < 2*initial_Cash:
        total += total * (procent/100)
        years += 1

    print("Twoja inwestycja podwoi swoją wartość po", years, "latach.")

main()
