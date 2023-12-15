list1 = []
for i in range(1000, 3000+1):
    a = str(i)
    #print(a)
    if (int(a[0])%2==0) and (int(a[1])%2==0) and (int(a[2])%2==0) and (int(a[3])%2==0) :
        list1.append(a)
z = ",".join(list1)
print("Even numbers are :", z)