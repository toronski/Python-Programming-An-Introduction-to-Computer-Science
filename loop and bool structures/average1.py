# average2.py   INTERACTIVE


'''
def main():
    total = 0.0
    count = 0
    moredata = "tak"

    while moredata[0] == 't':
        x = float(input("Wpisz numer >> "))
        total = total + x
        count = count + 1
        moredata = input("Masz więcej numerów (tak czy nie)? ")

    print("\nŚrednia z podanych numerów wynosi", total / count)

main()

'''

# average3.py   SENTINEL

'''
def main():
    total = 0.0
    count = 0
    x = float(input("Wpisz numer (negatywny, aby wyjść) >>"))

    while x >= 0:
        total = total + x
        count = count + 1
        x = float(input("Wpisz numer (negatywny, aby wyjść) >>"))

    print("\nŚrednia z podanych numerów wynosi", total / count)

main()
'''
'''
def main():
    total = 0.0
    count = 0
    xStr = input("Wpisz numer (<Enter> aby wyjść) >>")

    while xStr != "":
        x = float(xStr)
        total += x
        count += 1
        xStr = input("Wpisz numer (<Enter> aby wyjść) >>")
    print("\nŚrednia wpisanych numerów to", total / count)

main()

'''

# average5.py   FILE LOOP

'''
def main():
    fileName = input("W jakim pliku znajdują się liczby? ")
    infile = open(fileName, 'r')
    total = 0.0
    count = 0
    for line in infile:
        total += float(line)
        count += 1
    print("\nŚrednia numerów z pliku to", total / count)

main()
'''
'''
def main():
    fileName - input("W jakim pliku znajdują się liczby? ")
    infile = open(fileName, 'r')
    total = 0.0
    count = 0
    line = infile.readline()
    while line != "":
        total += float(line)
        count += 1
        line = infile.readline()
    print("\nŚrednia liczb z pliku wynosi", total / count)

main()
'''

# average7.py   NESTED

def main():
    fileName = input("W jakim pliku znajdują się liczby? ")
    infile = open(fileName, 'r')
    total = 0.0
    count = 0
    line = infile.readline()
    while line != "":
        for xStr in line.split(','):
            total += float(xStr)
            count += 1
        line = infile.readline()
    print('\nŚrednia z liczb w pliku wyniesie', total / count)

main()
