n = int(input("Enter number of levels  :"))
for i in range(n+1):# no: of rows
    for j in range(n-i):# Spacing (blank space ddecrement)
        print('', end=' ')
    for k in range(i):# * printing

        print(k, end=' ')
    print()