
name_original = 'Jon Snow'
name_new = name_original
name_original = 'Jaehaerys Targaryen'
print(name_original, name_new)

#The above works for simple data types like strings, integers, floats, booleans ->
#Not for lists

#To copy lists you need to use slicing

list_original = [1, 2, 3]
list_new = list_original[:]
list_original[0] = -5
print('Orginal:', list_original, '\nNew:', list_new)

#Or if we wanted a fragment
list_original = [1, 2, 3]
list_new = list_original[:2]
list_original[0] = -5
print('Orginal:', list_original, '\nNew:', list_new)
