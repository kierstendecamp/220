def user_names():
    first_name = eval(input("enter first name: "))
    last_name = eval(input("enter last name: "))
    first_letter = first_name[0]
    last_seven = last_name[:7]
    print("username: " + first_letter + last_seven)

user_names()

def month():
    months = "janfebmaraprmayjunjulyaugsepoctnovdec"
    num_months = eval(input("enter a month: "))
    start_index = num_months * 3 - 3
    stop_index = start_index + 3
    the_month = months[start_index : stop_index]
    print("that is " + the_month)

month()