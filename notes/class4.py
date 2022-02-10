import math

# dot notation
result = math.sqrt(9)
print(result)
result = math.pow(2,3) # parameters | arguments
result_1 = 2 ** 3.0
print(result_1)

my_range = range(10)
my_range = range(3, 10) # start , stop
my_range_1 = range(3,10,1) # start , stop , step
my_range_2 = range(10,3)
print(list(my_range))

# accumulator pattern
my_sum = 0
for i in range(101):
    my_sum = my_sum + 1
print(my_sum)

# factorial 6! = 6 * 5 * 4 * 3 * 2 * 1 = 720
# print factorial use -1 to descend values
# do not have to include 1 in stop command
user_input = eval(input("enter value to find factorial: "))
fact = 1
for i in range(user_input, 0, -1):
    fact = fact * i
    print(fact)




