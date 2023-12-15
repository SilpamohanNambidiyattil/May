""" Program to find product of numbers in a list using function?"""
def find_Product(num):
    product = 1
    for i in num:
        product = product*i
    return product

num = [1,2,3,4,5]
print("Given List :",num)
print("Product :", find_Product(num))