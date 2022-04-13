"""
Name: Kiersten DeCamp
lab12.py
The following code is my work.
problem: to use python graphics to create outputs.
"""
from random import randint


def find_and_remove_first(list, value):
    i = 0
    while i < len(list):
        print(list[i])
        i += 1
        if list[i] == value:
            list.pop(value[0])
            list[value[i]] = input('kiersten')
        print()


def good_input():
    value = input("enter a number: ")
    if value >= 0 and <= 10:
        print("good input")
    if value > 10:
        print('too high')
    if value < 10 :
        print("too low")



def num_digits(num):
    i = 0
    while num != i:
        num // 10
        i += 1
        return i
    i = 0
    while[i]:
        input(int("enter a number: "))
        if num < i:
            return num


def hi_lo_game():
    num = randint(0, 100)
    i = 7
    while num == int[i]:
        guess = input(int("guess a number 1 to 100: "))
    if guess == num:
        print("correct! you win in ", i + 1, "guesses.")
    if guess > num:
        print("too high!")
    if guess < num:
        print("too low!")
    else:
        print("you lost!, the number was", num)


