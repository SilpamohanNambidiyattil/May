"""program to print rectangle pattern"""
r = int(input("enter row  limit :"))
c = int(input("enter column limit :"))
for i in range(r):
    for j in range(c):
        print('*',end=' ')
        #print()
    print()
print("-------------------")
"""program to print hollow rectangle"""
for i in range(1,r+1):
    for j in range(1, c+1):
        if (i==1 or i==r or j==1 or j==c):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()