# futval_graph4.py

from graphics import *

def createLabeledWindow():
    window = GraphWin("Wykres wzrostu inwestycji", 320, 240)
    window.setBackground('white')
    window.setCoords(-1.75, -200, 11.5, 10400)
    Text(Point(-1, 0), ' 0.0K').draw(window)
    Text(Point(-1, 2500), ' 2.5K').draw(window)
    Text(Point(-1, 5000), ' 5.0K').draw(window)
    Text(Point(-1, 7500), ' 7.5K').draw(window)
    Text(Point(-1, 10000), ' 10.0K').draw(window)
    return window

def drawBar(window, year, height):
    bar = Rectangle(Point(year, 0), Point(year+1, height))
    bar.setFill('green')
    bar.setWidth(2)
    bar.draw(window)

def main():
    print("Ten program pokazuje wzrost inwestycji w przeciągu 10 lat")
    principal = float(input("Wpisz kwotę początkową: "))
    apr = float(input("Wpisze roczne oprocentowanie: "))

    win = createLabeledWindow()
    drawBar(win, 0, principal)
    for year in range(1, 11):
        principal = principal * (1 + apr)
        drawBar(win, year, principal)

    input("Aby wyjść, naciśnij <enter>.")
    win.close()

main()
