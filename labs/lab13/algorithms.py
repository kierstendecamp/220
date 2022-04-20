"""
Name: Kiersten DeCamp
algorithms.py
The following code is my work.
problem: to use python graphics to create outputs.
"""
from random import randint


def read_data(filename):
    my_list = []
    i = 0
    read_file = open(filename, 'r')
    line = read_file.readlines()
    while i == read_file:
        split = i.split(' ')
    while my_list == split:
        my_list.append(int(my_list))
        return my_list


def is_in_linear(search_val, values):
    i = 0
    while i <= len(values):
        if values[i] == search_val:
            return True
        else:
            return False


def selection_sort(values):
    for i in range(len(values)):
        list_1 = i
        for j in range(i + 1, len(values)):
            list_2 = j
            if values[i] > values[j]:
                print("enter list values: ")
                swap = values[list_1], values[list_2] == values[list_2], values[list_1]

    print(values)


def calc_area(rect):
    my_list = []
    for i in rect:
        my_list.append(i[0]*i[1])
    print(calc_area(rect))


def rect_sort(rectangles):
    for i in range(len(rectangles)):
        rect = []
        my_list = input("enter the amount of rectangles: ")
        for j in range(len(rect[i + 1])):
            height = input('enter the height of the rectangle: ')
            width = input("enter the width of the rectangle: ")
    print(rectangles)



