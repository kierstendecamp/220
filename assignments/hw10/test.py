"""
Name: kiersten decamp
hw10.py

Problem: <create a program without for loops.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import copy


def fibonacci(n):
    if n < 1:
        return None
    total = 2
    a = 1
    b = 1
    while total < n:
        previous = a
        a += b
        b = previous
        total += 1
        return a


def double_investment(principle, rate):
    time = 0
    amount = 0
    principle_2 = copy.deepcopy(principle)
    while amount <= 2 * principle_2:
        amount = (principle(1 + rate / 100))
        time += 1
        principle = amount
    return time


def syracuse():
    num = int(input("enter positive integer: "))
    print("Syracuse sequence starting with, num", "is: ", end='')
    while num != 1:
        print(num, end='')
        if num % 2 == 0:
            num // 2
        else:
            num = 3 * num + 1
        print("1", ".")

"""
Name: kiersten decamp
hw10.py

Problem: <create a program without for loops.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math


class Spheres:

    def __init__(self, radius):
        self.radius = radius
        self.area = 0
        self.volume = 0


def get_radius(self):
    return self.radius


def surface_area(self):
    rad = self.radius
    self.area = 4 * math.pi * (rad * rad)
    return self.area


def volume(self):
    rad = self.radius
    self.volume = (4/3) * math.pi * (rad * rad * rad)
    return self.volume

  from graphics import Circle, Line


class Face:
    def __init__(self, window, center, size):
        eye_size = 0.15 * size
        eye_off = size / 3.0
        mouth_size = 0.8 * size
        mouth_off = size / 2.0
        self.window = window
        self.head = Circle(center, size)
        self.head.draw(window)
        self.left_eye = Circle(center, eye_size)
        self.left_eye.move(-eye_off, -eye_off)
        self.right_eye = Circle(center, eye_size)
        self.right_eye.move(eye_off, -eye_off)
        self.left_eye.draw(window)
        self.right_eye.draw(window)
        point_1 = center.clone()
        point_1.move(-mouth_size / 2, mouth_off)
        point_2 = center.clone()
        point_2.move(mouth_size / 2, mouth_off)
        self.mouth = Line(point_1, point_2)
        self.mouth.draw(window)

    def smile(self, window, center, size):
        def __init__(self, window, center, size):
            eye_size = 0.15 * size
            eye_off = size / 3.0
            mouth_size = 0.8 * size
            mouth_off = size / 2.0
            self.window = window
            self.head = Circle(center, size)
            self.head.draw(window)
            self.left_eye = Circle(center, eye_size)
            self.left_eye.move(-eye_off, -eye_off)
            self.right_eye = Circle(center, eye_size)
            self.right_eye.move(eye_off, -eye_off)
            self.left_eye.draw(window)
            self.right_eye.draw(window)
            point_1 = center.clone()
            point_1.move(-mouth_size / 2, mouth_off)
            point_2 = center.clone()
            point_2.move(mouth_size / 2, mouth_off)
            self.mouth = Line(point_1, point_2)
            self.mouth.draw(window)

    def shock(self):
        def __init__(self, window, center, size):
            eye_size = 0.15 * size
            eye_off = size / 3.0
            mouth_size = 0.8 * size
            mouth_off = size / 2.0
            self.window = window
            self.head = Circle(center, size)
            self.head.draw(window)
            self.left_eye = Circle(center, eye_size)
            self.left_eye.move(-eye_off, -eye_off)
            self.right_eye = Circle(center, eye_size)
            self.right_eye.move(eye_off, -eye_off)
            self.left_eye.draw(window)
            self.right_eye.draw(window)
            point_1 = center.clone()
            point_1.move(-mouth_size / 2, mouth_off)
            point_2 = center.clone()
            point_2.move(mouth_size / 2, mouth_off)
            self.mouth = Circle(center, size)
            self.mouth.draw(window)

    def wink(self):
        def __init__(self, window, center, size):
            eye_size = 0.15 * size
            eye_off = size / 3.0
            mouth_size = 0.8 * size
            mouth_off = size / 2.0
            self.window = window
            self.head = Circle(center, size)
            self.head.draw(window)
            self.left_eye = Line(center, eye_size)
            self.left_eye.move(-eye_off, -eye_off)
            self.right_eye = Circle(center, eye_size)
            self.right_eye.move(eye_off, -eye_off)
            self.left_eye.draw(window)
            self.right_eye.draw(window)
            point_1 = center.clone()
            point_1.move(-mouth_size / 2, mouth_off)
            point_2 = center.clone()
            point_3 = center.clone()
            point_2.move(mouth_size / 2, mouth_off)
            point_3.move(mouth_size, 2, mouth_off)
            self.mouth = Line(point_1, point_2)
            self.mouth = Line(point_2, point_3)
            self.mouth.draw(window)

