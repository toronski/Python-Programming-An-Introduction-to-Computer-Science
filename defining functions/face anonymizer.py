# photo anonymizer.py

from graphics import *
from math import *

'''
def interface():
    Text(Point(1,3), ' Temperature in Celsius:').draw(win)
    input = Entry(Point(2,3), 5)
    input.setText('')
    input.draw(win)
    output = Text(Point(2,1),'')
    output.draw(win)
    button = Text(Point(1.5,2.0), "Convert It")
    button.draw(win)
    rectangle = Rectangle(Point(1,1.5), Point(2,2.5))
    rectangle.setOutline("black")
    rectangle.draw(win)
'''

def drawFace(center, size, win):
    # eyes
    leftPoint = center.clone()
    leftPoint.move(size/2, size/3)
    leftEye = Circle(leftPoint, -size/5)
    leftEye.setFill('black')

    rightPoint = center.clone()
    rightPoint.move(-size/2, size/3)
    rightEye = Circle(rightPoint, -size/5)
    rightEye.setFill('black')
    # face
    face = Circle(center, size)
    face.setFill('yellow')
    # mouth
    mouth = Polygon(Point(center.getX() -size/8, center.getY() -size/2),
                    Point(center.getX() -size/4, center.getY() -size/3),
                    Point(center.getX() +size/4, center.getY() -size/3),
                    Point(center.getX() +size/8, center.getY() -size/2))
    mouth.setFill('black')
    # draw
    face.draw(win)
    leftEye.draw(win)
    rightEye.draw(win)
    mouth.draw(win)

def faceNumber(win):
    total = 0
    keyNumber = int(win.getKey())
    while isinstance(keyNumber,int):
        total += keyNumber
        try:
            keyNumber = int(win.getKey())
        except:
            return total
        
def main():
    # wprowadz zdjęcie do przerobienia
    picture = input("Write name and extension of picture to load: ")
    center = Point(0,20)
    image = Image(center, picture)
    
    # narysuj okno programu
    width = image.getWidth()
    height = image.getHeight()
    win = GraphWin("face anonymizer", width, height+50)
    win.setBackground('white')
    win.setCoords(-200, -200, 200, 200)
    image.draw(win)
    
    # wskazanie twarzy
    text = Text(Point(0, -180), "Write number of faces to anonymize and press \
    <ENTER>")
    text.setSize(20)
    text.draw(win)
    
    # liczba twarzy do zakrycia
    n = faceNumber(win)
    text.setText('Now click on the center of the face and its edge')
    
    # pętla rysująca twarz
    for i in range(n):
        center = win.getMouse()
        center.draw(win)
        size = win.getMouse()
        size.draw(win)
        radius = sqrt(
            (center.getX() - size.getX())**2 \
            + (center.getY() - size.getY())**2)
        drawFace(center, radius, win)

    text2 = Text(Point(0, -195), '(click anywhere to escape)')
    text2.setSize(12)
    text.setText('Faces are anonymized!')
    text2.draw(win)
    
    # zamknięcie programu
    win.getMouse()
    win.close()

main()
