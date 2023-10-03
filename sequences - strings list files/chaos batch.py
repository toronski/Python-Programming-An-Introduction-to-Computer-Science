# chaos batch.py

def main():
    print("Program obrazuje zachowanie chaotyczne")

    # dostarcz nazwy plików
    in_numFile = input("W jakim pliku znajdują się liczby?")
    out_numFile = input("Do jakiego plku zapiszemy chaotycznie wygenerowane liczby: ")

    # otwórz pliki
    in_Num = open(in_numFile, 'r')
    out_Num = open(out_numFile, 'w')
                        
    # przetwórz każdą linijkę w pliku
    index = 0
    for line in in_Num:
        line = 3.9 * float(line) * (1 - float(line))
        print(line, file=out_Num)

    # zamykamy otwarte pliki
    in_Num.close()
    out_Num.close()

                     
main()
