'''
Kiersten DeCamp
Lab 7
The following code is my work.
problem: to use python graphics to create outputs.
'''


def weighted_avg(in_file_name, out_file_name):
    open_file = open(in_file_name, 'r')
    file = open_file.readlines()
    file_2 = open(out_file_name, 'w')
    average = 0
    count = 0
    for line in file:
        total_weight = 0
        total = 0

        split = line.split(":")
        numbers = split[1]
        names = split[0]
        string_split = numbers.split()

        for i in range(0, len(string_split), 2):
            weight = eval(string_split[i])
            grades = eval(string_split[i + 1])
            total_weight += weight
            total += weight * grades

        if total_weight < 100:
            response = names + "'s average: Error: The weights are less than 100. \n"
            file_2.write(response)
        elif total_weight > 100:
            response_2 = names + "'s average: Error: The weights are more than 100. \n"
            file_2.write(response_2)
        else:
            file_2.write(names + "'s average:" + str(total / 100) + "\n")
            average = average + total / 100
            count = count + 1

    class_avg = average / count
    file_2.write("class average: " + str(class_avg))
    open_file.close()
    file_2.close()


if __name__ == '__main__':
    weighted_avg("grades.txt", "avg.txt")