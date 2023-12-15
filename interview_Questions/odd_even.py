"""Let all odd numbers come before even numbers , and sort the odd numbers in ascending order and even numbers in descenting order?"""

#n = input("Enter a string number")
#print("Given string:",n)
a = [1,9,8,2,3,7,6,4,5,5]
#print("Given list :", a)
x = []
y = []
for i in  a :
    if (i % 2) == 0 :
        x.append(i)
    else :
        y.append(i)
print("even list:", x)
print("odd list:", y)
y.sort()
print("odd ascending",y)
x.sort(reverse=True)
print("even decending",x)
y.extend(x)
print(y)
#z= " ".join((y))
#print(z)
