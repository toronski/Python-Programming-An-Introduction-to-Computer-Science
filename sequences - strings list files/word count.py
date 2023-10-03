# word count.py
# program liczy linijki tekstu, słowa i znaki w pliku

def main():
    print("Program liczy linijki tekstu, słowa i znaki w pliku")

    # dostarcz nazwę pliku
    in_File = input("Jaki plik chcesz policzyć? ")

    # otwórz plik
    file = open(in_File, 'r')
    count_file =file.read()
                       
    # przetwórz każdą linijkę w pliku
    word_Count = 0
    letters_Count = 0
    for line in count_file:
        letters_Count += len(line)
        line_split = line.split()
        word_Count += len(line_split)
    lines = count_file.readlines()
    line_Count = len(lines)

    # zamykamy otwarte pliki
    count_file.close()
    print("W pliku jest ", line_Count, " linijek tekstu, ", word_Count, "słów i ",
          letters_Count, "znaków.")

                     
main()

'''

def main():
    filename = input("Wpisz nazwę pliku: ")

    file = open(filename, 'r')
    file_str = file.read()

    line_count = 1
    word_count = 0
    char_count = 0

    for ch in file_str:
        char_count += 1
        if ch.isspace():
            word_count += 1
        if ch == '\n':
            line_count += 1

    print("\nInformacje o pliku")
    print('Liczba linijek: ', line_count)
    print("Liczba słów: ", word_count)
    print("Liczba znaków: ", char_count)

main()
'''
