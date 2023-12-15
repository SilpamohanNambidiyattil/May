""" Python program to 1. list files in a directory
                      2. Count no: of files in a directory
                      3. list files in a directory with extension txt """

import os

list1 = os.listdir('C:/Users/user/PycharmProjects/Operators/Data Types/handfile/pro/Assignment')
print("List of files :", list1)
count = 0
for i in list1:
    count = count+1
print("no: of files :", count)
for i in list1:
    if i.endswith(".txt"):
        print('Files with extension .txt :',i)