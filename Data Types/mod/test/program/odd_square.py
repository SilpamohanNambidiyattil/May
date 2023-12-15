""" Use a list comprehension to square root each odd number in a list.
The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
"""

import math
l =[int(i) for i in  input("enter numbers :").split(',')]
print("Given list:",l)
x=[]
for i in l:
    if i%2!=0 :
        x.append(i)
print("Odd list :",x)
y = []
for i in x:
    y.append(math.sqrt(i))
print("Square root list :",y)
z=','.join(map(str,y))
print("Square root :",z)