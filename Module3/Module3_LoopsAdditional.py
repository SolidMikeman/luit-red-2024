# Understanding the "Pass" instruction
# You can use the pass instruction when you don't yet know what to put inside your loop's body, or when using "if" "elif" or "else" to prevent a syntax error during development

for a in range (1, 6):
    for b in range (1, 6):
        print(a, 'x', b, '=', a * b)

#This next example is rarely used in practice
i = 5
while i < 5:
    print(i)
    i += 1
else:
    print('else:', i)