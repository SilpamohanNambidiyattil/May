""" Python program to print even and odd numbers in an array"""
from array import *
import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10])
print(arr)
print("Array length:", len(arr))
for i in range(len(arr)):
    if (arr[i]%2==0):
        print(arr[i],end=' ')
print("\n")
for i in range(len(arr)):
    if (arr[i]%2!=0):
        print(arr[i],end=' ')


