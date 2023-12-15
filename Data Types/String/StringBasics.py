# Accessing or Indexing
print("**Accessing Each Characters called Indexing**")
str1= "hello World"
print(str1[0])
print(str1[4])
print(str1[-1]) # negative indexing (get in Reverse order)
print(str1[-2])
# String Slicing
print("**Accessing a word called String Slicing**")
print(str1[6:])
print(str1[:6])
print(str1[1:5]) # range [1:4] is wrong instead of 4 use  5
print(str1[:-1]) # Get all elements Except the last one
print(str1[:5:-1]) # reverse of world
print(str1[5::-1])# reverse of hello
print(str1[::-2])
print(str1[:-2])
print(str1[-2:])
