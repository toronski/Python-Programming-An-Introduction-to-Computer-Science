# archery scorer.py

from graphics import *
from math import *

def target(center, win):
    # white circle
    c1 = Circle(center, 25)
    c1.setFill('white')
    c1.setOutline('black')
    c1.draw(win)

    # black circle
    c2 = Circle(center, 20)
    c2.setFill('black')
    c2.draw(win)

    # blue circle
    c3 = Circle(center, 15)
    c3.setFill('blue')
    c3.draw(win)

    # red circle
    c4 = Circle(center, 10)
    c4.setFill('red')
    c4.draw(win)

    # yellow circle
    c5 = Circle(center, 5)
    c5.setFill('yellow')
    c5.draw(win)
    
def main():
    win = GraphWin("Tarcza łucznicza", 400, 440)
    win.setCoords(0,0,100,110)
    
    center = Point(50, 60)
    win.setBackground('white')
    text = Text(Point(50, 5), "Strzel w tarczę i zobacz\
 ile punktów zdobędziesz\n(kliknij w dowolne miejsce, aby zacząć)")
    text.setSize(15)
    text.draw(win)
    win.getMouse()
    
    score = 0
    text.setText("Punktacja: " + str(score)) 
    shooting_target = target(center, win)
    

    for i in range(5):
        shot = win.getMouse()
        point = Circle(shot, 0.5)
        point.setFill('red')
        point.draw(win)
        distance = sqrt((50 - shot.getX()) ** 2 + (60 - shot.getY()) ** 2)
        if distance <= 25:
            score += round(9 - 2*(distance // 5))
            text.setText("Punktacja: " + str(score))
        else:
            text.setText("Strzał poza tarczą, nie zdobyłeś żadnych punktów...")

    win.getMouse()
    text.setText("Zakończyłeś z wynikiem: " + str(score))
    
    win.getMouse()
    win.close()
main()
