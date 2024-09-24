#Parameters are various values passed to a function

input_numbers = [5.0, 3.5, 7.8, 9.9, 10.0]

def get_average(input_numbers):  # This is a parameter
    total_sum = 0.0  # Avoid using 'sum' as it is a built-in function
    for number in input_numbers:
        total_sum += number
    return total_sum / len(input_numbers)

average = get_average(input_numbers)  # Call the function to get the average
print(average)

def print_letter_count(text, letter): #Positional Arguement
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    print('Number of', letter, 'is', counter)

print_letter_count('Welcome', 'e')