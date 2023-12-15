n = int(input("Enter limit :"))
p=1
for i in range(1, n+1):
    for j in range(n-i):
        print('', end=' ')
    for k in range(i):
        ch= chr(64+p)
        print(ch, end=' ')
        p=p+1
    print()
print("________________________________________________________")
for i in range(65,70):
    for j in range(65,i+1):
        print(chr(j), end=' ')
    print()
print("___________________________________________________________")
for i in range(65,70):
    for j in range(65,i+1):
        print(chr(i), end=' ')
    print()