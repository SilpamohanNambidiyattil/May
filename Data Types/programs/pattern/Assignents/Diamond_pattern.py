n = int(input("Enter the limit  :"))
for i in range(n+1):
    for j in range(n-i):
        print('', end = ' ')
    for k in range(i):
        print('*', end = ' ')
    print()

for i in range(1, n):
    for j in range(i):
        print('', end = ' ')
    for k in range(n-i):
        print('*', end = ' ')
    print()