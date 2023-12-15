n = int(input("Enter number of levels  :"))
for i in range(n):# no: of rows
    for j in range(i+1):# Spacing (blank space ddecrement)
        print('*', end=' ')

    print()