def prime(n):
    flag = False
    for i in range(2,n):
        if n%i==0 :
            flag=True
    if flag==True:
        print(num,"is not prime")
    else:
        print(num,"is prime")
num = int(input("enter a number :"))
prime(num)

