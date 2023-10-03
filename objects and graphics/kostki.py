# kostki

from graphics import *

def main():
    win = GraphWin("kostki", 500, 500)
    win.setCoords(0, 0, 10, 10)


    cube1 = Rectangle(Point(9, 9), Point(7, 7))
    cube1.setFill('white')
    cube1.setOutline('black')

    cube2 = Rectangle(Point(1, 9), Point(3, 7))
    cube2.setFill('white')
    cube2.setOutline('black')

    cube3 = Rectangle(Point(1, 1), Point(3, 3))
    cube3.setFill('white')
    cube3.setOutline('black')

    cube4 = Rectangle(Point(7, 3), Point(9, 1))
    cube4.setFill('white')
    cube4.setOutline('black')

    cube5 = Rectangle(Point(4, 6), Point(6, 4))
    cube5.setFill('white')
    cube5.setOutline('black')
    
    cube1.draw(win)
    cube2.draw(win)
    cube3.draw(win)
    cube4.draw(win)
    cube5.draw(win)

    '''

    class Cube:
        def __innit__(self, x1, y1, x2, y2):
            self.Rectangle(Point(x1, y1), Point(x2, y2))
            self.setFill('white')
            self.setOutline('black')
            self.draw(win)

    '''
    
main()
