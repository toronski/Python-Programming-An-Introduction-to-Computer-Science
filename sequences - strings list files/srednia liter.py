# srednia liter.py

def main():
    print("Preogram liczy średnią długość wyrazu w podanym zdaniu")

    zdanie = input("Wpisz swoje zdanie: ")
    word_list = zdanie.split() # dzielimy zdanie wyrazami

    letters = 0
    for word in word_list:
        letters += len(word) # bierzemy dlugosc kazdego slowa i dodajemy

    srednia = letters / len(word_list)

    print("Średnia długość słowa w podanym zdaniu to ", srednia)

main()
