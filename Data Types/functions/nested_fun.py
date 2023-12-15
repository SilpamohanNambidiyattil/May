def create_adder(x):
    def adder(y,z):
        return x+y+z
    return adder
add = create_adder(15)
print("sum :",add(2,3))# get all the properties of main function from add


""" Another method"""
def number1(a):
    def number2(b):
        return a*b
    return number2
print("product :",number1(2)(3))
