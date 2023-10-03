# drawFace.py

from graphics import *

def drawFace(center, size, win):
    # eyes
    leftPoint = center.clone()
    leftPoint.move(-size/2, -size/3)
    leftEye = Circle(leftPoint, size/5)
    leftEye.setFill('black')

    rightPoint = center.clone()
    rightPoint.move(size/2, -size/3)
    rightEye = Circle(rightPoint, size/5)
    rightEye.setFill('black')
    # face
    face = Circle(center, size)
    face.setOutline('black')
    face.setFill('grey')
    # mouth
    mouth = Polygon(Point(center.getX() -size/6, center.getY() -size/5),
                    Point(center.getX() -size/5, center.getY() +size/5),
                    Point(center.getX() +size/6, center.getY() -size/4),
                    Point(center.getX() +size/5, center.getY() +size/4))
    mouth.setOutline('black')
    mouth.setFill('white')

    face.draw(win)
    leftEye.draw(win)
    rightEye.draw(win)
    mouth.draw(win)

def main():

    win = GraphWin("Buzie w tym programie niezliczone :O", 600, 600)
    a = win.getMouse()
    b = win.getMouse()
    c = win.getMouse()
    
    drawFace(a, 23, win)
    drawFace(b, 66, win)
    drawFace(c, 100, win)
main()
