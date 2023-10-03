# moving bricks

from graphics import *

def main():
    win = GraphWin()
    shape = Rectangle(Point(50,50), Point(100,100))
    shape.setOutline('red')
    shape.setFill('red')
    shape.draw(win)
    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape2 = shape.clone()
        shape2.move(dx,dy)
        shape2.draw(win)
    text = Text(Point(100, 10), 'Click again to quit')
    text.draw(win)
    win.getMouse()
    win.close()

main()
