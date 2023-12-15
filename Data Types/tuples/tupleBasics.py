thistuple = ("apple", 89, 6, "banana")
print(thistuple)
print(thistuple[0])
print(thistuple[-1])
print(thistuple[0][-1])
print(thistuple[0][2:])
print(thistuple[0][:2])
print(thistuple[3][-1])
print(thistuple[3][2:5])

#add

tuple_1 = ("apple", "banana", "cherry", [8, "riya",0])
print(tuple_1)
x = tuple_1[3]
y = x[0]
print(x)
print(y)
z = list(tuple_1)
print(z)
co = z.copy()
print(co)
z.remove("apple")
print(z)
z.pop(2)
print(z)
newtup = (1,2, 1,4,6, 7, 4,1,)
c = newtup.count(1)
print(c)
b = newtup.index(7)
print(b)

t1 = ("silpa", "akshay")
t2 = ("mohan", "latha")
v = t1 + t2
print(v)
n = t1 *2
print(n)
t3 = ("apple", "banana", "cherry", [8, "riya", 0])
q = list(t3)
q.reverse()
print(q)