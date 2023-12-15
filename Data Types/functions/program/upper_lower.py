""" Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9"""
str1 = input("Enter  Sentence :")
print("Given Sentence : " ,str1)
upper = 0
lower = 0
for i in str1:
    if i.isupper()==True:
        upper = upper+1
    elif i.islower()==True:
        lower = lower+1
print("Number of upper case :", upper)
print("Number of lower case :", lower)