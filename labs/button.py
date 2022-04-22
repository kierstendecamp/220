
from graphics import *

class Button:
    # __init__(self, Rectangle shape, String label)
    # initializes shape and text. Label is a string used to create the Text object
    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(shape.getCenter(), label)

    # get_label() -> string - returns the text of the button
    def get_label(self):
        return self.text.getText()

    # set_label(label) -> void - update the button text
    def set_label(self, label):
        self.text.setText(label)

    # draw(win) -> void - draws the button with text on it
    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    # undraw() -> void - undraws the button as well as the associated label
    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    # is_clicked(point) -> bool - returns True if the point is within the button
    # (including the edges); otherwise, returns False.
    def is_clicked(self, point):
        p1 = self.shape.getP1()
        p2 = self.shape.getP2()
        click_x = point.getX()
        click_y = point.getY()
        return p1.getX() <= click_x <= p2.getX() and p1.getY() <= click_y <= p2.getY()

    # color_button(color) -> void - color the door with color
    def color_button(self, color):
        self.shape.setFill(color)
