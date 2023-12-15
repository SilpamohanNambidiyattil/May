num = int(input("Enter a number :"))
n1, n2 = 0, 1

print("Fibonacci")
for i in range(num+1):
    print(n1, end='')
    n_next = n1+n2
    n1 = n2
    n2 = n_next
    #print(n1, end='')

