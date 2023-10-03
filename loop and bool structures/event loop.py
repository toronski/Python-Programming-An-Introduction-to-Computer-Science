# event loop 1.py

from graphics import *

def handleKey(k, win):
    if k == 'r':
        win.setBackground('pink')
    elif k == 'w':
        win.setBackground('white')
    elif k == 'g':
        win.setBackground('lightgrey')
    elif k == 'b':
        win.setBackground('lightblue')

def handleClick(pt, win):
    entry = Entry(pt, 10)
    entry.draw(win)

    while True:
        key = win.getKey()
        if key == "Return": break
        elif key == "Escape":
            entry.undraw()
            return
            
    entry.undraw()
    typed = entry.getText()
    Text(pt, typed).draw(win)

    win.checkMouse()

def main():
    win = GraphWin("Okienko kolorów", 500, 500)

    while True:
        key = win.checkKey()
        if key == 'q':
            break
        if key:
            handleKey(key, win)
            
        pt = win.checkMouse()
        if pt:
            handleClick(pt, win)

    win.close()

main()
