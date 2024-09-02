#This is theoretical practice, but rarely used in practice
#In Python there are six bitwise operaators that allow you to manipulate bits of data
#&
#|
#~
#^
#<<
#>>

first_bit = 1
second_bit = 0

print(first_bit & second_bit) # & means "and"

print(first_bit | second_bit) # | means "or"

print(first_bit ^ second_bit) # ^ means exclusive or

print(~1) # ~ is a logical negation

print(12 << 1) #Should be able to run without print. In this example we shift to the left by a single bit
print(12 >> 2) #Shift right would be original value divided by two