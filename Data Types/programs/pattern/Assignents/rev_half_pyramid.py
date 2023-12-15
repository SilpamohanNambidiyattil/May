n = int(input("Enter number of levels  :"))
for i in range(n+1, 0, -1):
    for j in range(1,i):
        i=i-1
        print(i, end=' ')
    print()