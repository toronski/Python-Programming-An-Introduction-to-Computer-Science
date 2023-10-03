# quiz oceny.py

from graphics import *

def main():
    file = open('oceny2.txt', 'r')
    grades_str = file.readlines()
    count_list = [0]*26
    for num in grades_str:
        count_list[eval(num)] += 1

    # stworz okno graficzne
    win = GraphWin("Oceny uczniów", 300, 600)
    win.setCoords(-10, -10, 100, 120)
    win.setBackground('white')

    # narysuj histogram
    for i in range(26):
        text = Text(Point(-5 + i*10, -5), str(i))
        text.setSize(10)
        text.draw(win)
        height = count_list[i] * 100 / max(count_list)
        if count_list[i] != 0:
            bar = Rectangle(Point(-7.5 + i*10, 0), Point(-2.5 + i*10, height))
            bar.draw(win)

    # zamknij okno i plik
    win.getMouse()
    win.close()
    file.close()
    
main()
