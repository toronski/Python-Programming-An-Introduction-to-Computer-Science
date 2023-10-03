# kiedy wielkanoc.py

def easter(year):
    a = year % 19
    b = year % 4
    c = year % 7
    d = ((19*a) + 24) % 30
    e = ((2*b) + (4*c) + (6*d) + 5) % 7
    easterDate = 22 + d + e
    if easterDate > 31:
        april = easterDate - 31
        return str(april) + ' kwietnia.'
    else:
        return str(easterDate) + ' marca.'
    
def main():
    print("Program do obliczania daty Wielkanocy na podstawie podanego roku.")
    year = eval(input("Podaj rok: "))

    if 2048 >= year >= 1982:
        print("W ", year, " roku, Wielkanoc wypadnie ", easter(year))
    else:
        print("W takim roku? Panie, a kto to policzy!")

main()

        
