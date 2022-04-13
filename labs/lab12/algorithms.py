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




