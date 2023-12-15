def even(n):
    x = []
    for i in range(4,n+1):
        if (i % 2) == 0:
            x.append(i)
    return x
n=int(input("Enter the limit :"))
print("Even list :",even(n))

x = [i for i in range(4,31) if i%2==0]
print("list compre:",x)