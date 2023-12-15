""" Insertion of Array Elements"""
arr = [0,0,0]
arr[0]=1
arr[1]=2
arr[2]=3
#arr[3]=4
print("array elements:",arr)
print("________________________________")
#Another method using import module
from array import *
array1 = array('i', [1,2,3,4,5])
array1.insert(2,10)
print("Array insertion")
for x in array1:
    print(x,end=' ')
print("\n_____________________________________")


""" Deletion of Array Elements"""
array2 = array('i', [10,20,30,40,50])
#array2.remove(30)
array2.pop(1)
print("Array Deletion")
for x in array2:
    print(x, end=' ')
print("\n_____________________________________")


"""Searching of Array elements """
print("Searching Array Element(Display index position)")
print( array2.index(40))
print("\n_____________________________________")

""" Update Array"""
print("Update Array")
array2[3]=70
for x in array2:
    print(x, end=' ')
print("\n_____________________________________")


"""Append Array"""
print("Append ")
array2.append(90)
for x in array2:
    print(x, end=' ')
#print("\n_____________________________________")


