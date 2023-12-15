a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Given list :", a)
x = []
y = []
for i in  a :
    if (i % 2) == 0 :
        x.append(i)
    else :
        y.append(i)
print("even list:", x)
print("odd list:", y)
