num = int(input("Enter a number :"))
def fib(num):
    n1,n2 = 0,1
    for i in range(num):
        print(n1, end='')
        n_next = n1 + n2
        n1 = n2
        n2 = n_next
    return n1
print(fib(num))
