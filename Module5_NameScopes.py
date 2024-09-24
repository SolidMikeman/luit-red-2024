#When we say the scope of a name, we will refer to a variable name. 
#The scope of a name is the part of the code where the name is properly recognizable and can be used

def show_truth():
    mysterious_var ='New Suprise'
    print(mysterious_var)

mysterious_var = 'Suprise'
print(mysterious_var)
show_truth()
print(mysterious_var)