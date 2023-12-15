l1 = [2,4,3]
print("Given l1 :",l1)
l2 =[5,6,4]
print("Given l2 :",l2)

def list_rev(a,b):
    a.reverse()
    b.reverse()
    print("l1 reverse :",a)
    print("l2 reverse :",b)
    x=[]
    for i in a:
        x.append(str(i))
    print(x,end='')
    print('\n')
    y = []
    for i in b:
        y.append(str(i))
    print(y,end='')
    to_int(x,y)

def to_int(x,y):
    print('\n')
    #print(m)
    num1 = 0
    num2 =0
    for i in x:
        num1 = (num1 * 10) + (ord(i) - 48)
        #print(ord(i))
    print(num1)
    for j in y:
        num2 = (num2 * 10) + (ord(j) - 48)
        #print(ord(i))
    print(num2)
    a = num1 + num2
    print("sum :", a)
    rev = 0
    num = a
    while (num > 0):
        rem = num % 10
        # print(rem)
        rev = (rev * 10) + rem
        # print(rev)
        num = num // 10
    print("result :", rev)
list_rev(l1,l2)

