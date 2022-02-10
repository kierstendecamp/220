'''
Kiersten DeCamp
Lab 3
The following code is my work.
problem: to analyze traffic patterns.

'''


def traffic():
    num_of_roads = eval(input("what is the number of roads?: "))
    vehicles_accumulator = 0  # total number of cars over all roads and days

    for days in range(num_of_roads):
        print("what is the number of days road", days + 1, "surveyed?")
        num_of_days = eval(input(""))
        cars_accumulator = 0  # total number of cars per road

        for roads in range(num_of_days):
            print("what is the number of cars traveled on day", roads + 1, "surveyed?")
            cars_traveled = eval(input(""))
            cars_accumulator = cars_accumulator + cars_traveled
            vehicles_accumulator = vehicles_accumulator + cars_traveled
            print("average vehicles per day: ", cars_accumulator / num_of_days)

    print("total number of vehicles traveled on all roads: ", vehicles_accumulator)
    print("average cars traveled on all roads:", vehicles_accumulator / num_of_roads)


traffic()

