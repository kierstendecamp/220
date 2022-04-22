
from graphics import *

class Door:
    # __init__(self, Rectangle shape, String label)
    # initializes shape and text. Label is a string used to create the Text object
    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(shape.getCenter(), label)
        self.secret = False

    # get_label() -> string - returns the text of the door
    def get_label(self):
        return self.text.getText()

    # set_label(label) -> void - update the door text
    def set_label(self, label):
        self.text.setText(label)

    # draw(win) -> void - draws the door with text on it
    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    # undraw() -> void - undraws the door as well as the associated label
    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    # is_clicked(point) -> bool - returns True if the point is within the door
    # (including the edges); otherwise, returns False.
    def is_clicked(self, point):
        p1 = self.shape.getP1()
        p2 = self.shape.getP2()
        click_x = point.getX()
        click_y = point.getY()
        return p1.getX() <= click_x <= p2.getX() and p1.getY() <= click_y <= p2.getY()

    def open(self, color, label):
        self.color_door(color)
        self.set_label(label)

    def close(self, color, label):
        self.color_door(color)
        self.set_label(label)

    # color_button(color) -> void - color the door with color
    def color_door(self, color):
        self.shape.setFill(color)

    # is_secret() -> bool - returns True if the door is the secret door, otherwise False
    def is_secret(self):
        return self.secret

    # set_secret(secret) -> void - sets the door’s secret value
    def set_secret(self, secret):
        self.secret = secret
