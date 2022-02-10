

from graphics, import Point, Circle, Text, Polygon,
import math


win = GraphWin('Face', 700, 700)
win.setCoords(0, 0, 10, 10)

face_center = Circle(Point(5,8),3)
face = Circle(face_center, 350/2)
left_eye = Circle(Point(300, 125), 35)
right_eye = Circle(Point(400, 125), 35)

left_eye.setFill('yellow')
left_eye.setOutline('green')
left_eye.setWidth(10)
right_eye.setFill('blue')
right_eye.setOutline('red')
right_eye.setWidth(10)
win.setBackground("light blue")

Text(Point(350,600), "Bob")
name.draw(win)
face.draw(win)
left_eye.draw(win)
right_eye.draw(win)
click_point = win.get.Mouse()
click_point.
print(click_point.getX(), click_point.getY())







input('enter to close')


