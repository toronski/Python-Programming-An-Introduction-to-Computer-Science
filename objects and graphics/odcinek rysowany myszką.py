# rysujemy i mierzymy odcinek

from graphics import *
import math

def main():
    win = GraphWin('rysujemy i mierzymy odcinek', 400, 400)
    win.setBackground('white')
    
    point1 = win.getMouse()
    point2 = win.getMouse()

    # wyznaczamy wspolrzedne punktow
    x1value = point1.getX()
    y1value = point1.getY()
    x2value = point2.getX()
    y2value = point2.getY()

    # rysujemy linie i punkt srodkowy
    aLine = Line(Point(x1value, y1value), Point(x2value, y2value))
    aLine.draw(win)
    midPoint = aLine.getCenter()
    midPoint.setFill('cyan')
    midPoint.draw(win)

    # wyliczamy nachylenie i dlugosc
    dx = x2value - x1value
    dy = y2value - y1value

    if dx == 0:
        print("Linia pionowa - nie podzielimy przez '0'.")
    else:
        slope = dy / dx
        length = math.sqrt((dx ** 2) + ( dy ** 2))

        print("Nachylenie odcnika wynosi ", slope, ".")
        print("Długość odcinka wynosi ", length, ".")

main()
