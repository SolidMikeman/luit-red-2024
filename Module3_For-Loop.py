#Sequences in Python are special data structures that can store mre than one value and can be browsed sequentially, meaning element by element
#the "for" loop can be used to scan each element

for letter in 'hello!':     #the "in" in this line is used to introduce the range of possible values or the sequence that we should scan
    print('Current letter', letter)
#Scanning a sequance is often called iterating a sequence. Entering a loop's body once is called iteration

for counter in range(1,11): #the range is a very special function which generates the desired integer values for our control variable
    print(counter)
print('Finished!')

#There are 3 versions of the range function
# for counter in range(11) In this example 0 will be the start value and will end after 10

# for counter in range(1, 11) As shown before the start value will be 1 and will end after 10

for counter in range(1, 11, 2): # This will count every second number
    print(counter)
print('Finished!') 