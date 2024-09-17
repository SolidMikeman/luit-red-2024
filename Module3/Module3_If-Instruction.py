#Conditional statements or an "if" statement

user_age = int(input('What is your age? '))
if user_age > 30:     #If is a special instruction which introduces and if statement after a space. After the condition we need a colon 
    print('You are over 30 years old') #The recommendation is to always use exactly four spaaces as the indentation
    print('Sorry, you do not qualify') #These two invocations from aa so called block
elif user_age == 30:  #elif is short for else if. You can have as many elif statements as you want
    print('You are exactly 30 years old') 
    print('You will need to meet additional conditions to qualify')  
else:                 #An else block after an if staatement means when the condition is not met, do the following. You can have only one else statement in Python
    print('You are 30 years old or younger') #Note how the text is indented lines with if and else are not inented, but the lines following them are
    print('Congratulations, you qualify!')