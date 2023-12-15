new_list =[x for x in range(10) if x<5 ]
print(new_list)
mat = [[i for i in range(3)] for i in range(3)]
print(mat)
""" FUNCTION """
def name():
    print('hiiii')
name()

"""lambda"""
"""Sum of a and b"""
def sum(a,b):
    c=a+b
    print("sum :",c)
sum(2,3)
x = lambda a,b : a+b
print("sum :",x(2,1))
y= lambda a,b : a*b
print("product :",y(2,3))

"""map function"""
"""product of two list"""
n1 = [1,2,3]
n2 = [4,5,6]
result = map(lambda x,y: x*y, n1,n2)
print("product:",list(result))

"""Square  of a list"""
num =[1,5,3,4]
new_list = []
for i in num:
    new_list.append(i**2)
print("List Square:",new_list)
lam = lambda i : i**2
print( list(lam(num)))

z = map(lambda i: i**2, num)
print("Using map:", list(z))