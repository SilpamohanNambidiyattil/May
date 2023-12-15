""" 7.Write a Program to print duplicates from a list of integers """

l=[1,1,2,3,4,4,6,5,5,7]
print('Given List :',l)
dup=[]
same=[]
for i in l:
    if i not in same:
        same.append(i)
    elif i not in dup:
        dup.append(i)
print('Duplicates are :',dup)

""" 
OUTPUT
Given List : [1, 1, 2, 3, 4, 4, 6, 5, 5, 7]
Duplicates are : [1, 4, 5]
"""
