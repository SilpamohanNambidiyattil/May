n = int(input("Enter number of levels  :"))
for i in range( n+1):
    print('', end = ' ')
    for j in range(1, i+1):
        print(j, end=' ')
    print()