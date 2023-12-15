""" Use a list comprehension to square root each odd number in a list.
The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
"""

import math
l =[int(i) for i in  input("enter numbers :").split(',')]
print("Given list:",l)
x = [ i for i in l if i%2!=0]
print("odd list :",x)
y = [ math.sqrt(i) for i in x]
print("Square root:",y)
z = [math.pow(i,2) for i in x]
print("Square :",z)
