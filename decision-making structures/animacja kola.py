# animacja koła.py

from graphics import *
from math import *
from random import randrange

def main():
    win = GraphWin("latające koło", 500, 500)
    win.setBackground('white')

    text = Text(Point(250, 250), "Kliknij myszką aby rozpocząć animację.")
    text.setSize(15)
    text.draw(win)

    c1 = randrange(500)
    c2 = randrange(500)
    kolo = Circle(Point(c1, c2), 25)
    kolo.setWidth(3)
    kolo.setFill('black')

    dx = 1
    dy = 1
    
    win.getMouse()
    text.undraw()
    kolo.draw(win)

    for i in range(1000):
        center = kolo.getCenter()
        pointX = center.getX()
        pointY = center.getY()
        kolo.move(dx, dy)
        
        if pointX >= 500:
            dx = -abs(dx)
        elif pointY >= 500:
            dy = -abs(dy)
        elif pointX <= 0:
            dx = abs(dx)
        elif pointY <= 0:
            dy = abs(dy)
        update(30)

main()
