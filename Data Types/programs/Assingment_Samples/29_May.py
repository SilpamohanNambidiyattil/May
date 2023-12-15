""" program to print even lengthed words from a string """

n = input("enter string : ")
s = n.split(" ")
for i in s:
    if len(i) % 2 == 0:
        print(i)

print("_______________________________________")
""" python program to print the count of upper case and lower case letters in the string?? """

str_1 = input("enter the string :")
upper = 0
lower = 0
for i in str_1:
    if i.isupper()==True:
        upper= upper+1
    elif i.islower()==True:
        lower= lower+1
print("upper case count: ", upper)
print("lower case count :", lower)

