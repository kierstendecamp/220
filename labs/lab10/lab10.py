"""
Name: Kiersten DeCamp
lab10.py
"""
from graphics import *

def main(self,):
    win = GraphWin("test", 400, 400)
    rectangle = Rectangle(Point(100, 250), Point(300, 250), Point(100, 200), Point(300, 200))
    rectangle2 = Rectangle(Point(100, 50), Point(100, 150), Point(300, 50), Point(300, 150))
    win.getMouse()
    win.draw(rectangle)
    win.draw(rectangle2)
    button = Point((200, 200), "exit")
    door_button = Point((200, 150), "closed")




