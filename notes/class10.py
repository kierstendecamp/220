# chapter 6
# functions
import math
math.sqrt(9)


def sing(name):
    x = 3
    print("Happy Birthday to you")
    print("Happy Birthday to you")
    print("Happy Birthday dear kiersten")
    print("Happy Birthday to you")


def happy():
    print("happy birthday to you")

def sing_2():
    happy()
    happy()
    print("happy birthday dear{}!".format(name))
    happy()

# def <name>(<parameters>)
# <body>

sing("lindsay")
print()
sing("George")
print()

def distance(p1, p2):
    x1 = p1.getX()
    y1 = p1.getY()
    x2 = p2.getX()
    y2 = p2.getY()
    d = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    point_a = Point(2, 3)
    point_b = Point(100, 220)
    distance(point_a, point_b)
    print(d)
