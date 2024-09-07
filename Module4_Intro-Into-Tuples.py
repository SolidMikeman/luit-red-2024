#Tuples are similar to lists. They are created with ()

#One Element Tuple
one_el_tuple_a = (1,) #You can use round brackets in this example (optional)
one_el_tuple_b = 1, #Here we need a comma so Python understands we are trying to make a tuple and not an ordinary single value. 
three_el_tuple = 1, 2, 3 #When using more than one value in your tuple, the final comma is optional 

print(three_el_tuple)

#Mutability
#There are two kinds of data, mutable and immutable
#Mutable data can be freely updated anytime you want. Lists are a good example



#Immutable data can not be changed
user_data = ('Vladimir', 'Russian', 1980)
#user_data.append('teacher') #As we can see when run you can not append a Tuple
# Another example would be using del  You can not delete an element of a Tuple

#You can use slicing and indexing with Tuples, but not for changing them
print(user_data[0]) #This works
#print(user_data[0]) = 'Mark' #This does not

#Strings are also Immutable
message = 'Welcome'
message[0] = 'w' #You can not do this