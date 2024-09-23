#Adding elements to Dictionary
#--------------------------------
grades = {} #Empty dictionary
grades['John'] = 'A-'
grades['Anne'] = 'B'
grades['Anne'] = 'A' #Can change by adding new data
#print(grades)

#We can also us update method
grades.update({'John':'A'})
#print(grades)

#print(len(grades)) #Due to my version of Python I can't use without print

#To check if given key is present in a dictionary can use "in operaator"
#if 'John' in grades:
    #print('John got:', grades['John'])

#Can delete using del
#del grades['John']
#print(grades)

#How to Iterate dictionary
#---------------------------
#Just the keys
#for el in grades:
    #print(el)

#for el in grades.keys():
    #print(el)

#Get access to the values
#for el in grades.values():
    #print(el)

#Get access to key and value
#for el in grades.items():
    #print(el)

for person, grade in grades.items():
    print(person, 'got', grade)

