import math
import graphics


# how to create a point
my_point = graphics.Point(50,70)
point_a = graphics.Point(70,90)
# everytime you construct an object it gets an x and a y
x = point_a.getX()
y = point_a.getY()
# print(y)
# print(x+3)
# print(point_a.getX(), point_a.getY())    # accessor methods
point_a.move(10, 0)
# print(point_a.getX(), point_a.getY())


window = graphics.GraphWin("CSCI 220", 700,700)     # window
middle = graphics. graphics.Point(350,350)
middle.draw(window)
input("hit enter to close")

my_circle = Circle(middle, 70)
my_circle.draw(win)

input("hit enter to close")
import graphics


win = GraphWin('Face', 700, 700)
face_center = Point(350, 175)



input('enter to close')

