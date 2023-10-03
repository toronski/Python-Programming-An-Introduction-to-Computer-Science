# liczenie slow.py

def main():
    print("Program liczy słowa w zdaniu podanym przez użytkownika")

    zdanie = input("Wpisz zdanie: ")
    zdanie = zdanie.split()
    word_count = len(zdanie)

    print("Liczba słów w podanym zdaniu wynosi " + str(word_count))

main()
