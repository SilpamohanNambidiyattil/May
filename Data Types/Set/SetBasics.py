set1 = {"silpa", "python", 25, "mtech"}
print(set1)# unordered
set2 = {"silpa", "python", 25, "mtech", "python"}
print(set2)#removed duplicates
x = list(set1)
print(x)
print(x[0])

"""add to set"""
set3 = {"apple", "banana", "cherry"}
set3.add("orange")
print(set3)
set4 = {"grapes", "mango"}
set3.update(set4)
print(set3)

"""Remove from set"""
set3.remove("cherry")
print(set3)
set3.discard("mango")
print(set3)

x = set3.pop()
print(x)
print(set3)


set1 = {"silpa", "python", 25, "mtech",(1,2,3)}# we can use tuble inside
print(set)

""" isdisjoint()"""
check_set1 = {"silpa","reethu","aruna"}
check_set2 = {"mohan","akshay","latha","silpa"}
z = check_set1.isdisjoint(check_set2)
print(z)

y = check_set1.issubset(check_set2)
print(y)

