# triangle2.py

import math
from graphics import *

def square(x):
    return x ** 2

def distance(p1, p2):
    dist = math.sqrt(square(p2.getX() - p1.getX())
                    + square(p2.getY() - p1.getY()))
    return dist

def main():
    win = GraphWin("Narysuj trójkąt")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    win.setBackground('white')

    message = Text(Point(5, 0.5), "Kliknij w trzech miejscach")
    message.draw(win)

    # narysuj 3 wierzchołki trójkąta
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    # uzyj obiektu polygon, aby narysowac trojkat
    triangle = Polygon(p1, p2, p3)
    triangle.setFill('peachpuff')
    triangle.setOutline('cyan')
    triangle.draw(win)

    # oblicz obwod trojkąta
    perim = distance(p1, p2) + distance(p2, p3) + distance(p3, p1)
    message.setText("Obwód trójkąta wynosi: {0:0.2f}".format(perim))

    # czekaj na klikniecie, zeby wyjsc
    win.getMouse()
    win.close()

main()
