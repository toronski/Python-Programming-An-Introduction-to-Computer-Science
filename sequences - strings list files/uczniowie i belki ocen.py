# uczniowie i belki ocen.py

from graphics import *

def main():
    file = open('oceny.txt', 'r')
    n = eval(file.readline())

    # informacje o uczniach
    names = []
    grades = []
    for i in range(n):
        name, grade = file.readline().split()
        names.append(name)
        grades.append(eval(grade))

    # stworz okno
    win = GraphWin("Wizualizacja ocen uczniów", 400, n * 30)
    win.setCoords(-40, 0, 110, n)
    win.setBackground('white')


    # narysuj belki
    for i in range(n):
        text = Text(Point(-20, n - 0.5 - i), names[i])
        text.setSize(10)
        text.draw(win)
        bar = Rectangle(Point(0, n - 0.70 - i), Point(grades[i], n - 0.35 - i))
        bar.setOutline('black')
        bar.draw(win)

    # zamykamy okno i plik
    win.getMouse()
    win.close()
    file.close()


main()
