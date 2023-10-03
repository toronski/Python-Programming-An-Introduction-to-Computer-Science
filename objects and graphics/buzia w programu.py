# buzia w tym programu

from graphics import *

def main():
    win = GraphWin("Buzia w tym programu", 500, 500)

    hairUnder = Rectangle(Point(150, 150), Point(350, 235))
    hairUnder.setFill(color_rgb(243,216,42))
    hairUnder.setWidth(0)
    hairUnder.draw(win)

    face = Oval(Point(150, 150), Point(350, 400))
    face.setFill(color_rgb(255, 204, 153))
    face.draw(win)

    hair = Rectangle(Point(150, 150), Point(350, 210))
    hair.setFill(color_rgb(243,216,42))
    hair.setWidth(0)
    hair.draw(win)
    
    eyeLeft = Circle(Point(200, 240), 15)
    eyeLeft.setFill('white')
    eyeLeft.setOutline('black')
    eyeLeft.setWidth(1.5)
    eyeLeft.draw(win)
                     
    eyeRight = eyeLeft.clone()
    eyeRight.move(100, 0)
    eyeRight.draw(win)
                     
    leftMid = Circle(Point(200, 240), 7)
    leftMid.setFill(color_rgb(42,97,228))
    leftMid.draw(win)
                     
    rightMid = leftMid.clone()
    rightMid.move(100, 0)
    rightMid.draw(win)

    mouth = Oval(Point(225, 300), Point(275, 355))
    mouth.setOutline('black')
    mouth.setWidth(1)
    mouth.draw(win)
    mExp = Rectangle(Point(225, 300), Point(275, 325))
    mExp.setFill(color_rgb(255, 204, 153))
    mExp.setOutline(color_rgb(255, 204, 153))
    mExp.draw(win)

main()
