"""
Name: Kiersten DeCamp
hw2.py

Problem: to produce input and output using arithmetic.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math


def sum_of_threes():
    value  = eval(input("what is the value?: "))
    the_sum = 1
    for i in range(3,5):
        the_sum = the_sum + value + 1
        print(value*i, end="")
        sum_of_threes()


def multiplication_table():
    for i in range(1,11):
        for j in range(1,11):
    print(i * j, end='\t')
    print('')

def triangle_area():

    side_a = eval(input("what is the length of side a?:  "))
    side_b = eval(input("what is the length of side b?:  "))
    side_c = eval(input("what is the length of side c?:  "))
    sides = (side_a + side_b + side_c) / 2
    area = (math.sqrt(sides(sides - side_a)(sides - side_b)(sides - side_b)))
    print("the area is :", area)
    triangle_area()

def sum_squares():
    my_sum = 0
    for i in range(3,5):
        my_sum = my_sum + (i * i)
    print(sum)




def power():
    base = eval(input("what is the base of the function: "))
    the_power = eval(input("what is the power?: "))
    my_sum = 1
    for i in range(the_power):
        my_sum = my_sum * base
    print("my_sum", my_sum)

if __name__ == '__main__':
    pass
