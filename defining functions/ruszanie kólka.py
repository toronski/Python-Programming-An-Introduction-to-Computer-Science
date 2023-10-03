# ruszanie kółka

from graphics import *

def moveTo(shape, newCenter):
    oldCenter = shape.getCenter()
    dx = newCenter.getX() - oldCenter.getX()
    dy = newCenter.getY() - oldCenter.getY()
    shape.move(dx, dy)
    
def main():
    win = GraphWin('przesuwające się kółko', 500, 500)
    win.setBackground('white')
    circle = Circle(Point(250, 250), 40)
    circle.setOutline('cyan')
    circle.setFill('grey')
    circle.draw(win)
    
    text = Text(Point(250, 480), "Klikaj i ruszaj kółkiem!")
    text.setSize(20)
    text.draw(win)
    
    for i in range(10):
        newcenter = win.getMouse()
        moveTo(circle, newcenter)

    text.setText("Koniec tego klikania!")
    text.setSize(32)
    text.setTextColor('red')
    win.getMouse()
    win.close()
    
    
main()
