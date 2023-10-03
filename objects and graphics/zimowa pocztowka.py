# zimowa pocztówka


from graphics import *

def main():
    win = GraphWin('zimowa pocztówka', 1000, 500)
    win.setBackground(color_rgb(89,160,240))

    # snieg
    
    snow_floor = Rectangle(Point(0, 475), Point(1000, 500))
    snow_floor.setFill('white')
    snow_floor.setWidth(0)

    snow1 = Oval(Point(0, 450), Point(150, 500))
    snow1.setFill('white')
    snow1.setWidth(0)

    snow2 = Oval(Point(125, 461), Point(245, 500))
    snow2.setFill('white')
    snow2.setWidth(0)

    snow3 = Oval(Point(239, 459), Point(342, 489))
    snow3.setFill('white')
    snow3.setWidth(0)

    snow4 = Oval(Point(320, 460), Point(560, 500))
    snow4.setFill('white')
    snow4.setWidth(0)

    snow5 = Oval(Point(523, 445), Point(670, 499))
    snow5.setFill('white')
    snow5.setWidth(0)

    snow6 = Oval(Point(640, 461), Point(720, 500))
    snow6.setFill('white')
    snow6.setWidth(0)
    
    snow7 = Oval(Point(700, 440), Point(800, 499))
    snow7.setFill('white')
    snow7.setWidth(0)

    snow8 = Oval(Point(789, 451), Point(839, 482))
    snow8.setFill('white')
    snow8.setWidth(0)

    snow9 = Oval(Point(820, 460), Point(870, 490))
    snow9.setFill('white')
    snow9.setWidth(0)

    snow10 = Oval(Point(858, 456), Point(912, 489))
    snow10.setFill('white')
    snow10.setWidth(0)

    snow11 = Oval(Point(905, 440), Point(1000, 500))
    snow11.setFill('white')
    snow11.setWidth(0)
    
    
    snow_floor.draw(win)
    snow1.draw(win)
    snow2.draw(win)
    snow3.draw(win)
    snow4.draw(win)
    snow5.draw(win)
    snow6.draw(win)
    snow7.draw(win)
    snow8.draw(win)
    snow9.draw(win)
    snow10.draw(win)
    snow11.draw(win)

    # balwanek body

    snowman_bottom = Circle(Point(400, 450), 80)
    snowman_bottom.setFill('white')
    snowman_bottom.setWidth(0)

    snowman_middle = Circle(Point(400, 340), 60)
    snowman_middle.setFill('white')
    snowman_middle.setWidth(0)

    snowman_top = Circle(Point(400, 250), 45)
    snowman_top.setFill('white')
    snowman_top.setWidth(0)

    snowman_bottom.draw(win)
    snowman_middle.draw(win)
    snowman_top.draw(win)

    # guziczki

    guzik1 = Circle(Point(400, 340), 3.5)
    guzik1.setFill('black')
    guzik0 = guzik1.clone()
    guzik0.move(0, -20)
    guzik2 = guzik1.clone()
    guzik2.move(0, 20)
    guzik3 = guzik2.clone()
    guzik3.move(0, 20)
    guzik4 = guzik3.clone()
    guzik4.move(0, 20)
    guzik5 = guzik4.clone()
    guzik5.move(0, 20)
    guzik6 = guzik5.clone()
    guzik6.move(0, 20)
    guzik7 = guzik6.clone()
    guzik7.move(0, 20)

    guzik0.draw(win)
    guzik1.draw(win)
    guzik2.draw(win)
    guzik3.draw(win)
    guzik4.draw(win)
    guzik5.draw(win)
    guzik6.draw(win)
    guzik7.draw(win)
    
    # balwanek glowa

    eye_Left = Circle(Point(380, 227.5), 5)
    eye_Left.setFill('black')
    eye_Right = eye_Left.clone()
    eye_Right.move(40, 0)
    
    eye_Left.draw(win)
    eye_Right.draw(win)

    nose = Polygon(Point(400, 240), Point(400, 250), Point(440, 245))
    nose.setFill('orange')
    nose.setOutline('orange')
    nose.draw(win)

    # choinka

    pien = Rectangle(Point(800, 425), Point(830, 475))
    pien.setFill(color_rgb(153, 102, 51))
    pien.setWidth(0)
    pien.draw(win)

    tree_bottom = Polygon(Point(700, 445), Point(930, 445), Point(815, 345))
    tree_bottom.setFill(color_rgb(34, 134, 71))
    tree_bottom.setOutline(color_rgb(34, 134, 71))

    tree_middle = Polygon(Point(720, 380), Point(910, 380), Point(815, 300))
    tree_middle.setFill(color_rgb(34, 134, 71))
    tree_middle.setOutline(color_rgb(34, 134, 71))

    tree_top = Polygon(Point(740, 315), Point(890, 315), Point(815, 245))
    tree_top.setFill(color_rgb(34, 134, 71))
    tree_top.setOutline(color_rgb(34, 134, 71))


    tree_bottom.draw(win)
    tree_middle.draw(win)
    tree_top.draw(win)

    
main()
