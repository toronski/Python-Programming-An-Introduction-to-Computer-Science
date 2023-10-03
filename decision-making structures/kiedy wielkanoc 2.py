# data wielkanocy2.py

def easter(year):
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19*a + 24) % 30
    e = (2*b + 4*c + 6*d + 5) % 7
    day = 22 + d + e
    return day

def main():
    year = int(input("Wpisz rok pomiędzy 1982 a 2048: "))

    while year < 1900 or year > 2099:
        print("Zły rok.")
        year = int(input("Wpisz rok pomiędzy 1982 a 2048: "))

    if year == 1954 or year == 1981 or year == 2049 or year == 2076:
        day = easter(year) - 7
    else:
        day = easter(year)
        
    if day > 31:
        print("Wielkanoc wypada", day - 31, "kwietnia w", str(year), "roku.")
    else:
        print("Wielaknoc wypada", day, "marca w", str(year), "roku.")
        

main()

