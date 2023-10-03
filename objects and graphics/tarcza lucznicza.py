# rysowanie tarczy łuczniczej

from graphics import *

def main():
    win = GraphWin("Tarcza łucznicza", 400, 400)
    center = Point(200, 200)

    # white circle
    c1 = Circle(center, 100)
    c1.setFill('white')
    c1.setOutline('black')
    c1.draw(win)

    # black circle
    c2 = Circle(center, 80)
    c2.setFill('black')
    c2.draw(win)

    # blue circle
    c3 = Circle(center, 60)
    c3.setFill('blue')
    c3.draw(win)

    # red circle
    c4 = Circle(center, 40)
    c4.setFill('red')
    c4.draw(win)

    # yellow circle
    c5 = Circle(center, 20)
    c5.setFill('yellow')
    c5.draw(win)

main()
