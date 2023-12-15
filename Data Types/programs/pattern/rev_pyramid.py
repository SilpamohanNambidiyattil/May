n = int(input("Enter number of levels  :"))
for i in range(n+1):# no: of rows
    for j in range(i):# Spacing (blank space increment)
        print('', end=' ')
    for k in range(n-i):# * printing
        print('*', end=' ')
    print()