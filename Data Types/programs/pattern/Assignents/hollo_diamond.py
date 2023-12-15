n = int(input("Enter the limit  :"))
for i in range(1,n+1):# for loop for upper triangle   ( No: of rows )
    for j in range(n-i+1):# for spacing
        print('', end = ' ')
    for k in range(1, 2*i):# pattern printing
        if k==1  or k==2*i-1: # [k==1 for left]  [k==2*i-1  for right]
            print('*',  end=' ')
        else:
            print('', end=' ')
    print()
for i in range(n+1, 0, -1):
    for j in range(1, n-i+2):
        print('', end=' ')
    for k in range(1, 2*i):
        if k==1 or k==2*i-1:
            print('*', end=' ')
        else:
            print('', end=' ')
    print()


