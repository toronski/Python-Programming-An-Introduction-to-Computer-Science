# rysujemy i liczymy prostokąt

from graphics import *

def main():
    win = GraphWin("rysujemy i liczymy prostokąt", 400, 400)

    corner1 = win.getMouse()
    corner2 = win.getMouse()

    x1 = corner1.getX()
    y1 = corner1.getY()
    x2 = corner2.getX()
    y2 = corner2.getY()

    rectangle = Rectangle(Point(x1, y1), Point(x2, y2))
    rectangle.draw(win)

    length = x2 - x1
    width = y2 - y1

    area = length * width
    parameter = 2 * (length + width)

    print("Obwód wynosi ", parameter, '.')
    print("Pole wynosi ", area, '.')

main()
