#futval_graph.py

from graphics import *
'''
def main():
    # Introduction
    print("Program oblicza wartość inwestycji po 10 latach.")

    # Get principal and interest rate
    principal = eval(input("Wpisz kwotę początkową: "))
    apr = eval(input("Wpisz roczną stopę procentową: "))

    # Create a graphic window with labels on left edge
    win = GraphWin("Wykres wzrostu inwestycji", 320, 240)
    win.setBackground("white")
    win.setCoords(-1.75,-200, 11.5, 10400)
    Text(Point(20, 230), ' 0.0K').draw(win)
    Text(Point(20, 180), ' 2.5K').draw(win)
    Text(Point(20, 130), ' 5.0K').draw(win)
    Text(Point(20, 80), ' 7.5K').draw(win)
    Text(Point(20, 30), '10.0K').draw(win)

    # Draw bar for initial principal
    height = principal * 0.02
    bar = Rectangle(Point(40, 230), Point(65, 230-height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    # Draw bars for successive years
    for year in range(1, 11):
        # calculate value for the next year
        principal = principal * (1 + apr)
        # draw bar for this value
        xll = year * 25 + 40
        height = principal * 0.02
        bar = Rectangle(Point(xll, 230), Point(xll+25, 230-height))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    input("Press <enter> to quit")
    win.close()

main()

'''

#futval_graph2.py

'''
def main():
    # Introduction
    print("Program oblicza wartość inwestycji po 10 latach.")

    # Get principal and interest rate
    principal = float(input("Wpisz kwotę początkową: "))
    apr = float(input("Wpisz roczną stopę procentową: "))

    # Create a graphic window with labels on left edge
    win = GraphWin("Wykres wzrostu inwestycji", 640, 480)
    win.setBackground("white")
    win.setCoords(-1.75,-200, 11.5, 10400)
    Text(Point(-1, 0), ' 0.0K').draw(win)
    Text(Point(-1, 2500), ' 2.5K').draw(win)
    Text(Point(-1, 5000), ' 5.0K').draw(win)
    Text(Point(-1, 7500), ' 7.5K').draw(win)
    Text(Point(-1, 10000), '10.0K').draw(win)

    # Draw bar for initial principal
    bar = Rectangle(Point(0, 0), Point(1, principal))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    # Draw bars for subsequent years
    for year in range(1, 11):
        # calculate value for the next year
        principal = (principal * (apr * 0.01)) + principal
        # draw bar for this value
        bar = Rectangle(Point(year, 0), Point(year+1, principal))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    input("Press <enter> to quit")
    win.close()

main()

'''

#futval_graph3.py

from graphics import *


def drawBar(window, year, height):
    bar = Rectangle(Point(year, 0), Point(year+1, height))
    bar.setFill('green')
    bar.setWidth(2)
    bar.draw(window)

def main():
    win1 = GraphWin("obliczamy zarobek", 300, 300)
    win1.setCoords(0.0, 0.0, 3.0, 5.0)

    # interfejs
    
    Text(Point(1.5, 4.5), "Program oblicza wartość inwestycji po 10 latach.").draw(win1)

    Text(Point(1, 3.5), "Wpisz kwotę początkową ").draw(win1)
    kwota_start = Entry(Point(2.5, 3.5), 5)
    kwota_start.setText('')
    kwota_start.draw(win1)

    Text(Point(1, 2.5), "Wpisz roczną stopę procentową ").draw(win1)
    procent = Entry(Point(2.5, 2.5), 5)
    procent.setText('')
    procent.draw(win1)

    Rectangle(Point(1.25, 1.5), Point(1.75, 1)).draw(win1)
    button = Text(Point(1.50, 1.25), "wykres")
    button.draw(win1)

    win1.getMouse()

    kwota_start = float(kwota_start.getText())
    procent = float(procent.getText())

    # okno graficzne z wykresem
    
    win2 = GraphWin("Wykres wzrostu inwestycji", 640, 480)
    win2.setBackground("white")
    win2.setCoords(-1.75,-200, 11.5, 10400)
    Text(Point(-1, 0), ' 0.0K').draw(win2)
    Text(Point(-1, 2500), ' 2.5K').draw(win2)
    Text(Point(-1, 5000), ' 5.0K').draw(win2)
    Text(Point(-1, 7500), ' 7.5K').draw(win2)
    Text(Point(-1, 10000), '10.0K').draw(win2)

    # Draw bar for initial principal
    drawBar(win1, 0, kwota_start)
    for year in range(1,11):
        kwota_start = kwota_start * (1 + procent)
        drawBar(win1, year, kwota_start)

    input("Press <enter> to quit.")
    win.close()

    # Draw bars for subsequent years
    for year in range(1, 11):
        # calculate value for the next year
        kwota_start = (kwota_start * (procent * 0.01)) + kwota_start
        # draw bar for this value
        bar = Rectangle(Point(year, 0), Point(year+1, kwota_start))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win2)

    Text(Point(6.25, 9000), "kliknij aby wyjść").draw(win2)
    win2.getMouse()
    win2.close()
    win1.close()

main()

