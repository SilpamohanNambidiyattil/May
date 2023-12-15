a = [["Silpa", "Mohan"], ["Latha", "Akshay"]]
print("Given List:", a)
l = len(a)
print("Length of the given list:", l)
for i in range (l-1) :
    if (a[i][0]>a[i+1][0]) :
        a[i][0],a[i+1][0] = a[i+1][0],a[i][0]

print(a)
