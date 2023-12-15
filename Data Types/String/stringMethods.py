str1 = "Silpamohan"
print(str1.upper())
print(str1.lower())
print(str1.capitalize())
print(str1.upper())

str2 = "iam silpamohan"
x = str2.find("silpamohan")
print(x)

str3 = "hello world"
y= str3.split()
print(y)

str4 = ("sipa", "mohan")
z = "#".join(str4)
print(z)


name = "Hello, iam Silpamohan"
x = name.islower()
print(x)
y = name.isupper()
print(x)
z = name.isalnum()
print(z)
a = name.isalpha()
print(a)
b = name.isdecimal()
print(b)

print(len(name))

str_1 = "I like bananas"
re_str = str_1.replace("bananas", "apples")
print(re_str)
str_2 = " but apple are fav"
print(str_1+str_2)

print(list(str_1))
print(tuple(str_1))
print(set(str_1))

