#n = input("Enter a string :")
n ="1982376455"
a = list(n)
#print(type(a))
print(a)
x = []
y = []
for i in a:
    if int(i) % 2 == 0 :
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
z=''.join(y)
print("Rearranged String :",z)

