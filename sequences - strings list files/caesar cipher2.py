# szyfr cezara2.py

def main():
    print("Program szyfrujący wiadomości za pomocą szyfru cezara")
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    abcs = alphabet*2 + alphabet.upper()*2
    
    # wpisz wiadomość
    message = input("Wpisz swoją wiadomość: ")
    key = eval(input("Oraz wartość klucza: "))

    # zaszyfruj wiadomość
    coded = ''
    # for word in message.split():
    for ch in message:
        coded += abcs[abcs.find(ch) + key]
        # coded += ' '
    # coded = coded[:-1] 

    print(coded)
    
main()

    
