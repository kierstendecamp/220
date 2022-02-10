'''
Kiersten DeCamp
Lab 4
The following code is my work.
problem: To make a greeting card.

'''

from graphics import *


def greeting_card():
    win = GraphWin("heart", 700, 700)
    win.setCoords(0, 0, 10, 10)
    win.setBackground("pink")
    polygon = Polygon(Point(5, 6), Point(6, 8), Point(7, 8), Point(8, 7), Point(5, 2))
    polygon.draw(win)
    polygon_2 = Polygon(Point(5, 6), Point(4, 8), Point(3, 8), Point(2, 7), Point(5, 2))
    polygon_2.draw(win)
    polygon.setFill("hot pink")
    polygon_2.setFill("hot pink")
    polygon.setOutline("hot pink")
    polygon_2.setOutline("hot pink")
    message = Text(Point(5, 1), "Happy Valentine's Day")
    message.setStyle("bold")
    message.setTextColor("red")
    message.setSize(20)
    message.draw(win)
    arrow = Line(Point(3, 2), Point(4, 3.5))
    arrow.setArrow("last")
    arrow.setFill("red")
    arrow.setWidth(5)

    arrow.draw(win)

    for i in range(7):
        arrow.move(1, 2)
        time.sleep(.5)
    message_2 = Text(Point(9, .5), "click to close!")
    message_2.setTextColor("hot pink")
    message_2.draw(win)
    win.getMouse()
    win.close()






greeting_card()
