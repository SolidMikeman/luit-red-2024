#Boolean Operators

#and example
#user_age = int(input('What is your age? '))
#user_country = input ('What is your country? ')

#if user_age < 25 and user_country == 'Germany':
    #print('You can apply for a German student exchange progamme')
#else:
    #print('Sorry, you do not qualify')

#or example
#user_country = input ('What is your country? ')

#if user_country == 'Thailand' or user_country == 'Laos' or user_country == 'Cambodia':
    #print('You can apply for an ASEAN student exchange progamme')
#else:
    #print('Sorry, you do not qualify')

#not example
#user_country = input('Where do you come from? ')
#if not user_country == 'Japan':
    #print('You are not from Japan!')
#else:
    #print('You are from Japan')

#user_age = int(input('What is your age? '))
#user_country = input ('What is your country? ')

#if not user_country == 'Germany' and user_age < 25 or \
   #user_country == 'Germany' and user_age < 23:
    #print('You qualify!')
#else:
    #print('You don\'t qualify!') 

#Booleans have priorities like in math
# 1. not
# 2. and 
# 3. or

#Way to make more readable without changing meaning or our program

user_age = int(input('What is your age? '))
user_country = input ('What is your country? ')

if ((not user_country == 'Germany') and user_age < 25) or \
   (user_country == 'Germany' and user_age < 23) :
    print('You qualify!')
else:
    print('You don\'t qualify!') 