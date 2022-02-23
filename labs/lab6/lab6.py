'''
Kiersten DeCamp
Lab 6
The following code is my work.
problem: to use python graphics to create outputs.
'''
from graphics import *
import math


def vigenere():
    # window
    win_width = 400
    win_height = 400
    win = GraphWin("button", win_width, win_height)
    win.setBackground("white")

    # boxes
    message_1 = Entry(Point(250, 100), 30)
    message_1.draw(win)
    keyword = Entry(Point(250, 150), 20)
    keyword.draw(win)
    encode = Rectangle(Point(200, 200), Point(275, 250))
    encode.draw(win)
    text_box = Text(Point(240, 225), "Encode")
    text_box.draw(win)

    message_box = Text(Point(75, 100), "Message to code")
    message_box.draw(win)
    keyword_text = Text(Point(100, 150), "Enter Keyword")
    keyword_text.draw(win)

    win.getMouse()

    pull_text = message_box.getText().upper().replace(" ", "")
    pull_keyword = keyword.getText().upper().replace(" ", "")

    x = " "
    for i in range(len(pull_text)):
        message_num = ord(pull_text[i]) - 65
        print(message_num, end=" ")
        keyword_num = ord(pull_keyword[i % len(pull_keyword)]) - 65
        print(keyword_num, end=" ")
        num = (message_num + keyword_num) % 26
        message_letter = chr(num + 65)
        x = x + message_letter

    end = Text(Point(200, 350), x)
    end.draw(win)

    click = Text(Point(200, 375), "Click again to close")
    click.setTextColor("black")
    click.draw(win)
    win.getMouse()
    win.close()


vigenere()




