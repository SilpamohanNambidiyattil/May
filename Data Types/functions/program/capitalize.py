""" Write a program that accepts sequence of lines as input and prints the lines after making all
 characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT

"""

lines = []
while True:
    str1 = input()
    if str1=='':
        break
    else:
        lines.append(str1+'\n')
print(lines)
x = ''.join(lines)
#print("Given Sentence : " ,x)
for i in x:
    cap = x.upper()
print(cap)