"""
Name: Kiersten DeCamp
hw1.py

Problem: <completed hw 1>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def calc_rec_area():
    length = (eval(input("enter the length: ")))
    width = eval(input("enter the width: "))
    area = length * width
    print("area =", area)



def calc_volume():
    length = (eval(input("enter the length: ")))
    width = eval(input("enter the width: "))
    height = eval(input("enter the height: "))
    volume = length * width * height
    print("volume =", volume)



def shooting_percentage():
    total_shots = eval(input("enter total number of shot: "))
    shots_made = eval(input("enter total number of shots made: "))
    shot_percentage = (total_shots / shots_made) * 100
    print("shot_percentage =", shot_percentage)
    print("%")
def coffee():
    cost_per_pound = eval(input("enter cost of coffee per pound: "))
    shipping_cost = eval(input("enter cost of shipping per pound: "))
    fixed_cost = eval(input("enter fixed cost: "))
    coffee_per_pound = cost_per_pound + shipping_cost + fixed_cost
    pounds_purchased = eval(input("how many pounds of coffee would you like?: "))
    total = coffee_per_pound * pounds_purchased
    print("Your total is: ", total)



def kilometers_to_miles():
    num_of_kilometers = eval(input("How many kilometers did you travel?: "))
    conversion = 1.61
    km_to_miles = num_of_kilometers * conversion
    print(km_to_miles)






if __name__ == '__main__':
    pass