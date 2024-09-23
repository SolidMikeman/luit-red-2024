#List with multiple seperated elements
#cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
#print(cells[0]) #Note due to VSCode I'm unable to write this as it should be which is cells[0] there is no need for the print

# If I just want 'A1"
#print(cells[0][0])

#If I want "B1"
#print(cells[1][0])

#Let's use for loop to iterate the list and print its elements 
#cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
#for x in cells:
    #print('Element:', x)

#Using iterate for specific element 
#cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
#for x in cells:
    #for y in x:
         #print('Element:', y)

#Making a visual table
#table = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
#for row in table:
    #for cell in row:
         #print(cell, '', end='')
    #print()

table = [[i for i in range (1, 6)] for j in range (4)]
print(table)
