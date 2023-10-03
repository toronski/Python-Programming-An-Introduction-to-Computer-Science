# Program obliczający średnią z serii liczb wpisanych przez użytkownika.

def main():
    print("Program obliczający średnią z serii liczb wpisanych przez użytkownika.")
    n = eval(input("Z ilu liczb mam wyliczyć średnią: "))
    suma = 0

    for i in range(1, n+1):
        i = input("Podaj liczbę: ")
        suma = suma + float(i)

    srednia = suma / n
    print("Średnia z ", n, "liczb wynosi ", suma)

main()
        
