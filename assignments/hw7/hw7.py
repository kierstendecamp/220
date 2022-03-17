"""
Name: kiersten decamp
hw7.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from encryption import encode
from encryption import encode_better


def number_words(in_file_name, out_file_name):
    open_file = open(in_file_name, 'r')
    txt = open_file.read()
    new = open(out_file_name, 'a')
    splitting = txt.split
    count = 1
    for i in splitting():
        count = count + 1
        print(str(count) + " " + i, file=new)
    open_file.close()
    new.close()
    print(new)


def hourly_wages(in_file_name, out_file_name):
    input_file = open(in_file_name, "r")
    output_file = open(out_file_name, "a")
    read_file = input_file.read()
    mes = read_file.split("\n")
    for line in mes:
        line_split = line.split()
        wage = eval(line_split[2])
        hours = eval(line_split[3])
        pay = (wage * hours) + (1.65 * hours)
        print(line_split[0] + " " + line_split[1] + " " + pay, file=output_file)

    input_file.close()
    output_file.close()
    print(output_file)


def calc_check_sum(isbn):
    isbn = isbn.replace("-", "")
    my_sum = 0
    for i in range(10):
        value = eval(isbn[9-i])
        my_sum += (i+1) * value
    return my_sum


def send_message(file_name, friend_name):
    open_file = open(file_name, "r")
    name = open_file.read()
    new_file = open(friend_name + ".txt", "a")
    print(name.replace("\n", ""), file=new_file)

    open_file.close()
    new_file.close()
    print(friend_name)


def send_safe_message(file_name, friend_name, key):
    open_file = open(file_name, 'r')
    file = open_file.read()
    split_file = file.split("\n")
    new = open(friend_name + ".txt", 'a')
    for i in range(len(split_file)):
        e = encode(split_file[i], key)
        print(e.replace("\n", ""), file=new)

    open_file.close()
    new.close()
    print(friend_name)


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    message = open(file_name, 'r')
    mes_txt = message.read()
    key_file = open(pad_file_name, 'r')
    key = key_file.read()
    message_code = mes_txt.split()
    for i in message_code:
        encode_better(i, key, friend_name + ".txt")

    message.close()
    key_file.close()


if __name__ == '__main__':
    pass
