n = int(input("Enter row limit  :  "))
for i in range(n+1):
    for j in range(n-i):
        #print('',end=' ')
        if (i==0 and (j!=0 and j!= i-1 )) or (i==n//2 and j!= n-1) or (j==0 and (i<n//2 and i!=0)) or (j== n-1 and (i<n//2 and i != 0)):

