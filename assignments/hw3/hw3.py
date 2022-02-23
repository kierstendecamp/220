"""
Name: Kiersten DeCamp
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def average():
    num_grades = eval(input("what is the number of grades submitted?: "))
    total_grades = 0
    for i in range(1, num_grades + 1):
        grades = eval(input("what is the grade for the hw: "))
        total_grades = total_grades + grades
        average_score = total_grades / num_grades
    print(average_score)

average()

def tip_jar():
    pass


def newton():
    pass


def sequence():
        # for i in range(0,2):
            # print(i% + 1, "end ")
    # mod - allows for repeat
    #


def pi():
   # for i in range 100



if __name__ == '__main__':
    pass
