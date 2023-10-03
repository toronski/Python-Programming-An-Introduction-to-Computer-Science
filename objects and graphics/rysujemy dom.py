# budujemy dom

from graphics import *
from math import *

def main():
    win = GraphWin('budujemy dom', 500, 500)
    win.setBackground('white')
    
    text = Text(Point(250, 40), "Zbudujmy dom w 5 kliknięć myszką\n Najpierw ściany")
    text.setSize(15)
    text.draw(win)
    
    # rysunek bryly domu
    click1 = win.getMouse()
    click2 = win.getMouse()
  
    house_brick = Rectangle(click1, click2)
    house_brick.draw(win)

    # rysunek drzwi
    text.setText("Zbudujemy dom w 5 kliknięć myszką\nTeraz drzwi")

    click3 = win.getMouse()
    x1 = click1.getX()
    y1 = click1.getY()
    x2 = click2.getX()
    y2 = click2.getY()
    x3 = click3.getX()
    y3 = click3.getY()
    
    dx = x2 - x1
    dy = y2 - y1
    house_foundation = sqrt((dx ** 2) + (dy ** 2))
    doorWidth = (1/5) * house_foundation
    
    #topDoorLeft = Line(click3, Point((x3 - float(doorWidth / 2)), y3))
    #topDoorRight = Line(click3, Point((x3 + float(doorWidth / 2)), y3))

    topDoorLeftCorner = Point((x3 - float(doorWidth / 2)), y3)
    bottomDoorRightCorner = Point((x3 + float(doorWidth / 2)), y1)

    door = Rectangle(topDoorLeftCorner, bottomDoorRightCorner)
    door.draw(win)


    # rysunek okna
    text.setText("Zbudujemy dom w 5 kliknięć myszką\nCzas na okno")

    click4 = win.getMouse()
    x4 = click4.getX()
    y4 = click4.getY()

    copy_click4 = click4.clone()
    
    click4.move((doorWidth / 4), (doorWidth / 4))
    copy_click4.move(-(doorWidth / 4), -(doorWidth / 4))
    okno = Rectangle(click4, copy_click4)
    okno.draw(win)

    # rysunek dachu
    text.setText("Zbudujemy dom w 5 kliknięć muszką\nTeraz czas na dach")
    click5 = win.getMouse()
    
    dach = Polygon(click5, click2, Point(x1, y2))
    dach.draw(win)

    # wiadomosc koncowa
    text.setText("Dom wybudowany!\nKliknij myszką w dowolnym miejscu, aby wyjść")

    win.getMouse()
    win.close()

main()
