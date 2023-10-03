# Program do obliczania nachylenia prostej przechodzącej przez dwa punkty.

def main():
    print("Program obliczający nachylenie prostej przechodzącej przez dwa punkty.")

    x1 = eval(input("Współrzędne x1: "))
    y1 = eval(input("Współrzędne y1: "))
    x2 = eval(input("Współrzędne x2: "))
    y2 = eval(input("Współrzędne y2: "))

    if x1 == x2: print("x1 nie może być równe x2!")

    slope = (y2 - y1) / (x2 - x1)

    print("Nachylenie prostej wynosi: ", slope)

main()
