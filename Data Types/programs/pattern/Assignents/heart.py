n = int(input("Enter number of :"))
for i in range(1, n+1):# no: of rows
    for j in range(n-i):# Spacing (blank space ddecrement)
        print('', end=' ')
    for k in range(i):# * printing
        print('*', end=' ')
for i in range(1, n + 1):  # no: of rows
    for j in range(n - i):  # Spacing (blank space ddecrement)
            print('', end=' ')
    for k in range(i):  # * printing
            print('*', end=' ')
    print()