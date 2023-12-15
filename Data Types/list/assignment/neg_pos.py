A = [1, 7, -8, 6, -5, 2, -4, 0,0]
print("Given list:", A)
x = []
y = []
z = []
for i in A:
    if i > 0:
        x.append(i)
        #print(x)
    elif i == 0 :
        z.append(i)
    else:
        y.append(i)
        #print(y)
print("Negative list:", x)
print("Positive list:", y)
print("Zero list:", z)
