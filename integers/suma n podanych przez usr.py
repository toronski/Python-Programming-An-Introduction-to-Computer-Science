# Program sumujący 'n' liczb wpisanych przez użytkownika.

def main():
    print("Program sumujący 'n' liczb podanych przez użytkownika.")

    n = eval(input("Ile liczb mam zsumować: "))
    razem = 0

    for i in range(1, n+1):
        i = input("Podaj liczbę do zsumowania: ")
        razem = razem + int(i)

    print("Suma ", n, "liczb podanych przez użytkownika wynosi: ", razem)

main()
