"""
Name: Kiersten DeCamp
hw6.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math


def cash_converter():
    integer = eval(input("enter an integer: "))
    my_string = "that is ${dollars:.2f}"
    print(my_string.format(dollars=integer))


def encode():
    message = input("enter a message: ")
    key = eval(input("enter a key: "))
    for i in range(len(message)):
        number = ord(message[i])
        letter = chr(number + key)
        print(letter, end="")
    print()


def sphere_area(radius):
    area = (4 * math.pi) * (radius ** 2)
    return area


def sphere_volume(radius):
    volume = (4/3 * math.pi) * (radius ** 3)
    return volume


def sum_n(number):
    sum_1 = 0
    for i in range(1, number + 1):
        sum_1 += i
    print(sum_1)


def sum_n_cubes(number):
    sum_2 = 0
    for i in range(1, number + 1):
        sum_2 += i ** 3
    print(sum_2)


def encode_better():
    phrase = input("enter a phrase: ")
    ret = " "
    key_phrase = input("enter a key phrase: ")
    for i in range(len(phrase)):
        character = ord(phrase[i]) - 65
        letter = ord(key_phrase[i % len(key_phrase)]) - 65
        cipher_val = ((character + letter) % 58) + 65
        cipher_text = chr(cipher_val)
        ret+=cipher_text
    print(ret)


if __name__ == '__main__':
    cash_converter()
    encode()
    sphere_area(13)
    sphere_volume(13)
    sum_n(4)
    sum_n_cubes(3)
    encode_better()
