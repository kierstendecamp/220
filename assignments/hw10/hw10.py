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




