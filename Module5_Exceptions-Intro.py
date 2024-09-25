#try:
    #value = int(input('Enter an integer'))
    #print('the inverse of', value, 'is', 1/value)
#except:
    #print('You did not provide a number, so I will not calculate the inverse')

try:
    value = int(input('Enter an integer'))
    print('the inverse of', value, 'is', 1/value)
except ValueError:
    print('You did not provide a number, so I will not calculate the inverse')
except ZeroDivisionError:
    print('You provide zero and division by zero is not possible')