'''
Kiersten DeCamp
Lab 5
The following code is my work.
problem: to use python graphics and string to create outputs.
'''

from graphics import *
import math


def triange():
    win = GraphWin('Triangle', 300, 300)

    win.setCoords(0, 0, 10, 10)
    point_1 = win.getMouse()
    point_2 = win.getMouse()
    point_3 = win.getMouse()

    triangle = Polygon(point_1, point_2, point_3)
    triangle.setFill("blue")
    triangle.draw(win)
    win.getMouse()

    length_1x = point_3.getX() - point_2.getX()
    length_2x = point_2.getX() - point_1.getX()
    length_3x = point_1.getX() - point_3.getX()
    length_1y = point_3.getY() - point_2.getY()
    length_2y = point_2.getY() - point_1.getY()
    length_3y = point_1.getY() - point_3.getY()
    length_a = ((length_1x ** 2) + (length_1y ** 2) ** 0.5)
    length_b = ((length_2x ** 2) + (length_2y ** 2) ** 0.5)
    length_c = ((length_3x ** 2) + (length_3y ** 2) ** 0.5)
    length = length_a + length_b + length_c
    s = (length_a + length_b + length_c) / 2
    area = math.sqrt(s * (s - length_a) * (s - length_b)* (s - length_c))

    text_1 = Text(Point(5, 3), "length: " + str(length))
    text_1.setSize(10)
    text_1.draw(win)
    text_2 = Text(Point(5, 1.5), "Area: " + str(area))
    text_2.setSize(10)
    text_2.draw(win)

    win.getMouse()
    win.close()

triange()

def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2 + 20, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 100, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")
    red_box = Entry(Point(win_width / 2 - 40, win_height / 2 + 40), 10)
    red_box.draw(win)


    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")
    green_box = Entry(Point(win_width / 2 - 40, win_height / 2 + 70), 10)
    green_box.draw(win)




    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")
    blue_box = Entry(Point(win_width / 2 - 40, win_height / 2 + 100), 10)
    blue_box.draw(win)


    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    for i in range(5):
        win.getMouse()
        red_amount = red_box.getText()
        red = eval(red_amount)
        green_amount = green_box.getText()
        green = eval(green_amount)
        blue_amount = blue_box.getText()
        blue = eval(blue_amount)
        shape.setFill(color_rgb(red, blue_amount, green_amount))



    # Wait for another click to exit
    win.getMouse()
    win.close()


color_shape()

def process_string():
    string = (input("enter a string: "))
    character_1 = string[0]
    print("first character: ", character_1)
    character_end = string[-1]
    print("last character: ", character_end)
    character_middle = string[2:5]
    print("characters 2-5: ", character_middle)
    beg_end = character_1 + character_end
    print("first and last characters: ", beg_end)
    first_three = string[0:3]
    print(first_three * 10)
    for character in string:
        print(character)
    print("number of characters in string: ", len(string))

process_string()

def process_list():
    pt = Point(5,10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = values
    print(x[1] + x[3])
    print("5 + 2.5 =", x[0] + x[2])
    print(x[1] * 5)
    print("[", x[2], ",", x[3], ",", x[4], "]")
    print("[", x[2], ",", x[3], ",", x[0], "]")
    print("[", x[2], ",", x[0], ",", eval(x[5], "]"))
    print("x = ", x[0] + x[2], + eval(x[5]))
    print("number of items in values", len(x))



process_list()

def another_series():
    terms = int(input("enter how many terms: "))
    my_sum = 0
    for i in range(terms):
        my_list = [2, 4, 6, 2, 4, 6]
        start = [0]
        stop = [terms - 1]
        product = my_list[start: stop]
        the_sum = my_sum + i
    print("sum =", the_sum)


another_series()

def target():
    win = GraphWin('target', 300, 300)
    win.setBackground('gray')
    center = 150
    diameter = 30
    first = Circle(Point(150, 150), center)
    first.setFill('white')
    first.setOutline('black')
    first.draw(win)
    second = Circle(Point(150, 150), center - diameter)
    second.setFill('black')
    second.setOutline('black')
    second.draw(win)
    third = Circle(Point(150, 150), center - 2 * diameter)
    third.setFill('blue')
    third.setOutline('black')
    third.draw(win)
    fourth = Circle(Point(150, 150), center - 3 * diameter)
    fourth.setFill('red')
    fourth.setOutline('black')
    fourth.draw(win)
    fifth = Circle(Point(150, 150), center - 4 * diameter)
    fifth.setFill('yellow')
    fifth.setOutline('black')
    fifth.draw(win)
    close = Text(Point(50, 10), "Click to close!")
    close.setTextColor("white")
    close.setSize(10)
    close.draw(win)
    win.getMouse()
    win.close()


