#Using the "in" operator to check for given element in a list

#invited_guests = ['Kate', 'Adam', 'Kerry', 'Joe', 'Anne', 'Bob']
#name = input('What is your name? ')
#if name in invited_guests:
    #print('Welcome!')
#else:
   #print('You are not invited!')

#Another version
invited_guests = ['Kate', 'Adam', 'Kerry', 'Joe', 'Anne', 'Bob']
name = input('What is your name? ')
if name not in invited_guests:
    print('You are not invited!')
else:
    print('Welcome!')