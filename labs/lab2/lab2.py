'''
Kiersten DeCamp
Lab 1
The following code is my work.
'''


def means():
    num_of_values = eval(input("enter the number of values: "))
    rms_accumulator = 0
    harmonic_accumulator = 0
    geo_counter = 1
    for i in range(num_of_values):
        values = eval(input("what is the value: "))
        square_values = values ** 2
        rms_accumulator += square_values
        harmonic_accumulator = harmonic_accumulator + (1 / values)
        geo_counter = geo_counter * values

    harmonic_mean = num_of_values / harmonic_accumulator
    rms_accumulator = rms_accumulator / num_of_values

    rms = rms_accumulator ** 0.5
    geo_mean = geo_counter ** (1 / num_of_values)

    print("what is the rms_average?: ", rms)
    print("what is the harmonic mean?: ", harmonic_mean)
    print("what is the geometric mean?: ", geo_mean)

means()




