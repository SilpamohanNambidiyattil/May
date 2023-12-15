"""foound of not"""
t1 = ("apple", "banana", "cherry")
if "apple" in t1 :
    print("yes")

"""convert tuple to string"""
t2 = ("s","t","r","i","n","g")
x = list(t2)
print(x)
print(''.join(x))

"""Count the occurence of 50 from the tuple"""
tuple1 = (20, 50, 78, 50, 60)
y = tuple1.count(50)
print(y)
v = enumerate(t2)
b = (list(v))
print(b)
tuple2 = (1,2,3,4,5,6,0)
print(all(tuple2))
print(any(tuple2))
l= len(tuple2)
print(l)
