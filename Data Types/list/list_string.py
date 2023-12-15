s = ['p', 'y', 't', 'h', 'o', 'n']
print("Given list:", s)
x = ''.join(s)
print("using join:", x)

str1 = ""
for i in s :
    str1 = str1 + i
print("using for loop:", str1)