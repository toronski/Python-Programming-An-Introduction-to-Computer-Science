# rysujemy trójkąt po kliknięciu myszką

from graphics import *

def main():
    win = GraphWin("Narysuj trójkąt")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Kliknij na trzy punkty")
    message.draw(win)

    # Get and draw three verticals of triangle

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    # Use Polygon object to draw the triangle

    triangle = Polygon(p1, p2, p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)

    # Wait for another click to exit
    message.setText("Kliknij gdziekolwiek, żeby wyjść.")
    win.getMouse()

main()
