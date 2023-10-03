# chaos.py

def main():
    print("Program obrazuje zachowanie chaotyczne")

    # wpisz liczby
    x, y = eval(input("\nWpisz po przecniku dwa numery pomiędzy 0 a 1: "))
    z = eval(input("Podaj liczbę iteracji: "))

    # tabela
    tytul = "index {0:5} {1:11}".format(x, y)
    print(tytul)
    print("-" * (len(tytul) + 3))
          
    # wylicz chaotycznie
    index = 0
    for i in range(z):
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)
        index = index + 1
        print("{0:3} {1:10.6f}{2:12.6f}".format(index, x, y))

main()
