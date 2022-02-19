"""
Name: Kiertsen DeCamp
HW5.py

Problem: use strings and lists to create outputs

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def name_reverse():
    name = (input("enter your name: "))
    x = name.split()
    first_name = x[0]
    last_name = x[1]
    print(last_name, ",", first_name)


def company_name():
    company = input("enter company name with a three part domain: ")
    word = company.split(".")
    print(word[1], end="")


def initials():
    num_students = eval(input("enter the number of students in the class: "))
    for i in range(num_students):
        f_name = input("enter students first name: ")
        l_name = input("enter students last name: ")
        print("initials: ", f_name[0] + l_name[0])


def names():
    name = eval(input("enter full names, separated by commas: "))
    name_list = name.split(', ')
    print("initials: ", end=" ")
    for i in name_list:
        initial = i.split(" ")
        print(initial[0][0]+initial[1][0], end=" ")


def thirds():
    number = eval(input("enter number of sentences: "))
    sentence = []
    for i in range(number):
        sentences = input("enter sentence" + str(i + 1) + ":")
        sentence.append(sentences)
    for i in sentence:
        output = ""
        for j in range(0, len(i), 3):
            output = output + i[j:j+1]
        print(output)
        output = ""


def word_average():
    total = 0
    word = input("enter a sentence: ")
    x = word.split()
    number = len(x)
    for i in x:
        total = total + len(i)
    average = total / number
    print(average)


def pig_latin():
    sentence = eval(input('enter a sentence to convert to pig latin: '))
    word = sentence.split()
    new = ""
    for i in word:
        new += i[1:]+i[0]+"ay "
        new = new.lower()
    print(new)


pig_latin()

if __name__ == '__main__':
    name_reverse()
    company_name()
    initials()
    names()
    thirds()
    word_average()
    pig_latin()

