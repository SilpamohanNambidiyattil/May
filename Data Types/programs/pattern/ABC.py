#for i in range(65, 91):
#    print(chr(i), end=' ')

n = int(input("Enter limit :"))
k=1
for i in range(n+1):
    for j in range(i):
        ch = chr(64+k)
        print(ch, end=' ')
        k = k+1
    print()