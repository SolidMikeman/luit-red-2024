def get_average(input_numbers):  # This is a parameter
    sum = 0.0  # Avoid using 'sum' as it is a built-in function
    for number in input_numbers:
        sum += number
    average = sum / len(input_numbers)
    return average

print('The average is:', get_average ([5.0, 3.5, 7.8, 9.9, 10.0]))

average = get_average([5.0, 3.5, 7.8, 9.9, 10.0])
if average > 5.0:
    print('The average is too high!')