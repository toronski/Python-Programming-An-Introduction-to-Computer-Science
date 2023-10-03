# szyfr cezara.py

def main():
    print("Program szyfrujący wiadomości za pomocą szyfru cezara")

    message = input("Wpisz swoją wiadomość: ")
    key = int(input("Oraz wartość klucza: "))


    coded = ''
    for ch in message:
        coded += chr(ord(ch) + key)

    print(coded)
    
main()
