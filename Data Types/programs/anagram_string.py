str1 = input("Enter 1st string :")
str2 = input("Enter 2nd string :")
str1 = str1.lower()
str2 = str2.lower()
x = list(str1)
x.sort()
y = list(str2)
y.sort()
print(x)
print(y)
if x==y:
    print("yes")
else:
    print("not")





