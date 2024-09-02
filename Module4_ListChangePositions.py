#first = input('Enter first number: ')
#second = input('Enter second number: ')
#print('Before swapping:', first, second)
#first = second
#second = first
#print('After swapping:', first, second)
#As we can see the above doesn't work.

#To fix we can use a third variable to store the first variable so we don't lose it
#first = input('Enter first number: ')
#second = input('Enter second number: ')
#print('Before swapping:', first, second)
#temporary = first
#first = second
#second = temporary 
#print('After swapping:', first, second)
#The above works fine, but Python has a shortcut. Let's try it out.

#first = input('Enter first number: ')
#second = input('Enter second number: ')
#print('Before swapping:', first, second)
#first, second = second, first
#print('After swapping:', first, second)

#This above is much simpler, and we can also use it for list elements.
#top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
#top_cities[0], top_cities[4] = top_cities[4], top_cities[0]
#print(top_cities) 

#We can also arrage alpahbetically
#top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
#top_cities.sort()
#print(top_cities)

#We can also arrange numerically from least to greatest
#random_numbers = [2, 5, 0, -3, 4]
#random_numbers.sort()
#print(random_numbers)

#To sort greatest to least or from Z to A
random_numbers = [2, 5, 0, -3, 4]
random_numbers.sort(reverse=True)
print(random_numbers)

#Remember when using sort, there's no coming back. You may want to sort lists temporarily, but also want to keep the original list order. ->
#To that end you use a general list function instead of a list method 

top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
print(sorted(top_cities))
print(top_cities)