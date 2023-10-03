# trojkat

from graphics import *
from math import *

def main():
    win = GraphWin("rysujemy i liczymy trojkat", 400, 400)

    x1 = 150
    y1 = 200
    x2 = 300
    y2 = 250
    x3 = 200
    y3 = 320

    triangle = Polygon(Point(x1, y1), Point(x2, y2), Point(x3, y3))
    triangle.draw(win)

    # dlugosci bokow
    dx1 = x2 - x1
    dy1 = y2 - y1
    length1 = sqrt((dx1 ** 2) + (dy1 ** 2))
    length1 = round(length1, 2)
    
    dx2 = x3 - x2
    dy2 = y3 - y2
    length2 = sqrt((dx2 ** 2) + (dy2 ** 2))
    length2 = round(length2, 2)
    
    dx3 = x3 - x1
    dy3 = y3 - y1
    length3 = sqrt((dx3 ** 2) + (dy3 ** 2))
    length3 = round(length3, 2)

    s = ((length1 + length2 + length3) / 2)
    area = sqrt(s * (s - length1)*(s - length2)*(s - length3))
        
    perimeter = length1 + length2 + length3

    print("Obwód wynosi ", perimeter, '.')
    print("Pole wynosi ", area, '.')

main()

