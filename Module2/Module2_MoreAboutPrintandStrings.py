#len('Hello!') I should be able to run this without print, but VScode isn't capable it seems
print(len('Hello!')) 

#Keyword Arguments and Named Arguments
print('Hello, World', end='! ') #End argument
print('Python speaking!')

#Sep Argument specifies the seperator between the values printed to the output
first_name = 'John'
print('Your first name is', first_name, 'Welcome!')

first_name = 'John'
print('Your first name is', first_name, 'Welcome!', sep= '-')

#You can use sep and end together 
first_name = 'John'
print('Your first name is', first_name, 'Welcome!', sep= '-', end='! ' )