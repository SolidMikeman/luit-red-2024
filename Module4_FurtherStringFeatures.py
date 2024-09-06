#You can using indexing and slicing with Strings
fav_band = 'Bring Me the Horizon'
print(fav_band[6])

print(fav_band[:5])

#You can not use indexing to change individdual characters within a string
#fav_band[6] = 'W'

#Upper & Lower
text = 'please capitalize me'
text_cap = text.upper()
print(text_cap)

#Return True or Flase
user_number = input('Please provide a number: ')
if user_number.isnumeric():
    print('Thank you, that\'s a correct number!')
else:
    print('Sorry', user_number, 'is not a number!')