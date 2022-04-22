"""
Name: Kiersten DeCamp
lab11.py
The following code is my work.
problem: create three door game
"""

from graphics import *
from door import Door
from button import Button
from lab10 import lab10
from random import randint


def main():
    win = GraphWin("Three Door Game", 700, 900)
    win.setBackground("light blue")
    rectangle = Rectangle(Point(100, 500), Point(200, 200))
    rectangle.setFill("brown")
    door1 = Door(rectangle, "Door 1")
    door1.draw(win)
    rectangle2 = Rectangle(Point(300, 500), Point(400, 200))
    rectangle2.setFill("brown")
    door2 = Door(rectangle2, "Door 2")
    door2.draw(win)
    rectangle3 = Rectangle(Point(500, 500), Point(600, 200),)
    rectangle3.setFill('brown')
    door3 = Door(rectangle3, "Door 3")
    door3.draw(win)
    secret_door_mess = Text(Point(350, 600), "click to guess the secret door!")
    message = Text(Point(350, 150), "I have a secret door!")
    score_box = Rectangle(Point(100, 100), Point(200, 150))
    score_text = Text(Point(120, 80), "wins")
    score_text.draw(win)
    score_text2 = Text(Point(170, 80), "losses")
    score_text2.draw(win)
    score0 = Text(Point(125, 125), "0")
    score0.draw(win)
    score_0 = Text(Point(175, 125), "0")
    score_0.draw(win)
    line = Polygon(Point(150, 100), Point(150, 150))
    quit_box = Rectangle(Point(500, 100), Point(550, 150))
    quit_mess = Button(quit_box, "QUIT")
    secret_door_mess.draw(win)
    quit_mess.draw(win)
    message.draw(win)
    score_box.draw(win)
    line.draw(win)
    get = win.getMouse()

    while not quit_box.is_clicked():
        door = [door1, door2, door3]
        rand_door = randint(0, len(door), -1)
        door[rand_door].set_secret(True)

    for i in door:
        if i.is_clicked(get) and i.is_secret():
            i.color_door('light green')
            win += 1
            point = win.getMouse()
        elif i.is_clicked() and not i.is_secret():
            i.color_door('red')
            score_text2.setText(str(score_text))
            get = win.getMouse()

        elif not i.is_clicked(get) and i.is_secret():
            i.color_door('light green')
            point = win.getMouse()

    if quit_mess.is_clicked(get):
        return win.close()

    win.getMouse()


main()
