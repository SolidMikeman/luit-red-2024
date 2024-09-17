#Loops are used to repeat an instruction or many instructions more than once

#while loops
#counter = 1
#while counter < 11:
    #print(counter)
    #counter += 1 #here it is important to increment the value of the variable inside to prevent an infinite loop
#print('Finished')

secret_number =14
print('''
==========================
=== SECRET NUMBER GAME ===
==========================
''')
user_input = int(input('Try to guess the secret number from 0 to 20: '))
while user_input != secret_number:
    print('Wrong!')
    user_input = int(input('Try and guess the secret number from 0 to 20: '))
print('Perfect! You have guessed the secret number.')