# program obliczający przekrój koła przez z linią horyzontalną

from graphics import *
from math import *

def main():

    # funkcja tworzaca linie
    def line_Y(y):
        line = Line(Point(-10, float(y)), Point(10, float(y)))
        line.draw(win)

    # input uzytkownika
    radius = eval(input("Podaj promień koła: "))
    line = eval(input("Podaj wysokośc lini horyzontalnej: "))

    # graf
    win = GraphWin("wizulizacja", 400, 400)
    win.setCoords(-10, -10, 10, 10)
    win.setBackground('white')
    circle = Circle(Point(0, 0), float(radius))
    circle.draw(win)
    line_Y(line)

    # punkty przeciecia kola
    try:
        point1 = float(sqrt((radius ** 2) - (line ** 2)))
        point2 = float(-sqrt((radius ** 2) - (line ** 2)))
        inter1 = Point(point1, line)
        inter2 = Point(point2, line)

        point1 = (point1, line)
        point2 = (point2, line)

        print("Dwa punkty przecinające koło to: ", point1, 'i', point2)

    except: print("BłĄD - koło nie przecina linii.")
    
main()
