# akronimy.py

def acronym(phrase):
    litery = ''
    for i in phrase:
        litery = litery + i[0]

    litery = litery.upper()
    return litery
    
def main():
    print("Program do tworzenia akronimów")

    wyrazenie = input("Wpisz wyrażenie, z którego chcesz zrobić akronim: ")
    slowa = wyrazenie.split(' ')

    print("Twój akronim to: ", acronym(slowa))

main()
