#Creating long lists using loops

#numbers = []
#for i in range(1, 101):
    #numbers.append(i)
    #print(numbers)

#An easier more space effective method
#numbers = [i for i in range(1, 101)]
#print(numbers)

#List comprehensions can be more complicated then this

numbers = [i for i in range(1, 101) if i % 3 != 0]
print(numbers)