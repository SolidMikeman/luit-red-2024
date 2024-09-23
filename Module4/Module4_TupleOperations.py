#You can use the len function to count number of elements in a tuple
#user_data = ('John', 'American', 1964)
#print(len(user_data))

#You can use the IN and NOT IN operators the same way as with lists
user_data = ('John', 'American', 1964)
if 'American' in user_data:
    print('This person is from the US!')

#Can use Iterate a tuple with a FOR loop
user_data = ('John', 'American', 1964)
for element in user_data:
    print(element) 

#Tuples can also be added together or multiplied by an integer
user_data = ('John', 'American', 1964) + ('Teacher', 'male')
print(user_data)

numbers = (0, 1) * 10
print(numbers)

