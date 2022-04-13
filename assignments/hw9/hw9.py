"""
Name: kiersten decamp
hw9.py

Problem: <create a hangman game.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from random import randint


def get_words(file_name):
    open_file = open(file_name)
    my_list = []
    for i in open_file:
        my_list.append(i)
    return my_list


def get_random_word(words):
    get_word = words[randint(0, len(words))]
    return get_word


def letter_in_secret_word(letter, secret_word):
    for i in range(len(secret_word)):
        if letter == secret_word[i]:
            return True
    return False


def already_guessed(letter, guesses):
    for i in range(len(guesses)):
        if letter == guesses[i]:
            return True
        return False


def make_hidden_secret(secret_word, guesses):
    ret = ""
    for i in range(len(secret_word)):
        test = False
        for j in range(len(guesses)):
            if secret_word[i] == guesses[j]:
                ret += guesses[j]
                test = True
        if test:
            ret += "_"
    return ret


def won(guessed):
    for i in range(len(guessed)):
        if "_" == guessed[i]:
            return False
        return True


def play_graphics(secret_word):
    while not secret_word:
        guess = input("guess a letter")
    finished = "_" * secret_word
    if finished:
        return True
    else:
        return str("try again")



def play_command_line(secret_word):
    if won:
        return print("you won")
    else:
        return str("you lost, play again")


if __name__ == '__main__':
    pass
    # play_command_line(secret_word)
    # play_graphics(secret_word)
