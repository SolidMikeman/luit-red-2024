#There are two important keywords that influence how your loop's body is executed 
#They are break and continue.

#Break: When Python encounters a break instruction it immediately exits the loop and moves on to the next instruction outside the loop
while True: # "while True:" will cause an infinite loop without the break instruction
    name = input('Enter your name or EXIT to close the program: ')
    if (name == 'EXIT'):
        break
    print('Hello', name)

#Continue: Is used to escape the current iteration and move on to the next one

for i in range(1, 21):
    if i % 5 == 0:
        continue
    print(i)