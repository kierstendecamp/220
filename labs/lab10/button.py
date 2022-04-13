"""
Name: Kiersten DeCamp
lab10.py
"""

from graphics import *
class button:

    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(shape.getCenter(), label)

    def get_label(self):
        return self.text.getText()

    def set_label(self, label):
        self.text.setText(label)

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self, win):
        self.shape.undraw(win)
        self.text.undraw(win)


    def is_clicked(self, point):
        point1 = self.shape.getP1()
        point2 = self.shape.getP2()
        x1 = point1.getX()
        y1 = point2.getY()
        x2 = point1.getX()
        y2 = point2.getY()
        if x1 is <= point.getX() <= x2 and y1 is <= point.getY() <= y2:
            return True
        else:
            return False

    def color_button(self, color):
        self.shape.setFill(color)

