""" Program to find product of numbers using Arbitrary Arguments"""
def find_Product(*numbers): # no:of arguments unknown
    product = 1
    for i in numbers:
        product = product*i
    return product
print("Product :", find_Product(2,3))
print("Product :", find_Product(2,3,2))

""" Program to find sum of two numbers using Default values """
def find_Sum(a=5,b=2):
    sum = a+b
    return sum
print("Sum of a abd b :", find_Sum()) # with a=5 and b=2
print("Sum of a abd b :", find_Sum(2,2)) # with a=2 and b=2
print("Sum of a abd b :", find_Sum(a=4)) # assign  a=4 and take value of b as default value 2 ( fun call with 1 argument)

""" Program with Keyword Argument"""
def name(f_name,l_name):
    print('First Name :', f_name)
    print('Last Name :', l_name)
name(f_name='Silpamohan',l_name='N')
name(l_name='Silpamohan', f_name='N')