""" lambda function
    small anoymous  function
    for small expressions"""
def sum(a,b):
    c=a+b
    d=a*b
    print(c)
    print(d)
sum(5,4)
""" using lambda function"""
x = lambda a,b : a+b #multiple  arguments is allowed but multiple expressions denied
y = lambda a,b : a*b
print(x(4,5))
print(y(2,2))

""" map reduce filters are build in functions"""
"""Map
    pairing of elements 
    """
# multiply list elements
number1=[1,2,3]
number2=[4,5,6]
mul = map(lambda x,y: x*y , number1,number2)
print(list(mul))

nums=[1,5,3,4]
sqr=[]
for i in nums:
    sqr.append(i**2)
print(sqr)
"""list compher"""
sqr1 =[i**2 for i in nums]
print(sqr1)

""" map"""
sqr2= map(lambda x:x**2,nums)
print(list(sqr2))


""" filter
    filter elements according to the condition"""
""" filter -ve numbers """
nu=[-3,-6,-5,2,5,6,-2]
neg = filter(lambda x:x<0,nu)
print(list(neg))

""" even"""
def even(n):
    if n%2==0:
        return True
    return False
n=[1,2,3,4,5,6,7,8,9]
e = filter(even,n)
print(list(e))

#l=['a','b','c','d']
#def vo(l):

""" reduce"""
from functools import reduce
list1=[1,3,4,5]
p = reduce(lambda x,)
