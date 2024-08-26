#Converting String number into Float number

#float() The float function accepts one arguement, a string, and the function tries to convert that value
#Method One Below
#height_cm = input('Height converter: enter your height in cm:')
#float_height_cm = float (height_cm)
#print('Your height in feet is:', float_height_cm / 30.48)

#Method Two Below
#height_cm = float(input('Height converter: enter your height in cm:'))
#print('Your height in feet is:', height_cm / 30.48 )

#If using an integer instead of float use int()
#year_born = int(input('What year were you born?'))
#print('In 2100, you will be', 2100 - year_born, 'years old') 

#You can convert a float or interger into a string using str()
temp_c = input('Enter the temperature today in Celsius degrees: ')
temp_f = float(temp_c) * 1.8 + 32
temp_statement = str(temp_c) + ' degrees Celsius equals ' + str(temp_f) + ' degrees Fahrennheit.'
print(temp_statement)