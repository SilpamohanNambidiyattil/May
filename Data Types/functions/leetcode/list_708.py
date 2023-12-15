l1 = [2,4,3]
print("Given l1 :",l1)
l2 =[5,6,4]
print("Given l2 :",l2)
l1.reverse()
l2.reverse()
print("l1 reverse :",l1)
print("l2 reverse :",l2)
x=[]
for i in l1:
    x.append(str(i))
print(x, end='')
print('\n')
y=[]
for i in l2:
    y.append(str(i))
print(y, end='')
print('\n')
num1 = 0
num2 = 0
for i in x:
    num1 = (num1*10)+(ord(i)-48)
    #print(ord(i))
print(num1)
print(type(num1))
for i in y:
    num2 = (num2*10)+(ord(i)-48)
    #print(ord(i))
print(num2)
a=num1+num2
print("sum :",a)
rev = 0
num = a
while (num>0):
    rem = num%10
    #print(rem)
    rev = (rev*10)+rem
    #print(rev)
    num = num//10
print("result :",rev)
