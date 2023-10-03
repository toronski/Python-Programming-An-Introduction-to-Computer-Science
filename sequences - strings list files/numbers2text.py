# numbers2text.py

# program konwertujacy sekwencje liczb unicode na tekst

def main():
    print("Program konwertuje sekwencję liczb Unicode na litery")

    # wiadomosc do odszyfrowania
    inString = input("Wpisz wiadomość w formacie Unicode: ")

    # pętla
    chars = []
    for numStr in inString.split():
        codeNum = eval(numStr)
        chars.append(chr(codeNum))

    message = ''.join(chars)
    print("\nRozszyfrowana wiadomość to: ", message)

main()
