#Collections aka Container Data Types
#A collection in Python is a data type that can store more than one value in a single variable
# We will learn 3 types of collections: lists, tuples, and dictionaries

#lists: empty_list = []

top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
#print(top_cities) 
#Remember List indices start at 0

print(top_cities[0]) #Due to version of Python on VSCode I'm not able to run with just top_cities[0]
#This is called Indexing above

print(top_cities[-1]) #Python is unique in that you can use negative indices

#Slicing
print(top_cities[0:2]) #Due to version of Python on VSCode I'm not able to run with just top_cities[0:2]
print(top_cities[2:])
print(top_cities[:3])
print(top_cities[:])