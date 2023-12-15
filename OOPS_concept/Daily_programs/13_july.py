""" 1. Simple Decorator program"""
# def dec(func):
#     def inner():
#         print("Decorator inner function")
#         func()
#     return inner
# @dec
# def normal_func():
#     print("Normal function")
# normal_func()
"""
___OUTPUT___
Decorator inner function
Normal function
"""

""" 2. Decorating functions with parameters"""
# def dec(func):
#     def inner(a,b):
#         print(f"iam going to divide {a} and {b}")
#         if b==0:
#             print(f"can't divide {a} and {b}")
#             return
#         return func(a,b)
#     return inner
# @dec
# def divide(a,b):
#     print(f"Result of {a} / {b}:",a/b)
# divide(4,2)
# divide(4,0)
"""
___OUTPUT___
iam going to divide 4 and 2
Result of 4 / 2: 2.0
iam going to divide 4 and 0
can't divide 4 and 0
"""

""" 3. Chaining decorators"""
def star(func):
    def inner(msg):
        print("*"*10)
        func(msg)
        print("*"*10)
    return inner
def symbol_(func):
    def inner(msg):
        print("_"*10)
        func(msg)
        print("_"*10)
    return inner
@star
@symbol_
def display(msg):
    print(msg)
display("hai silpa !")
"""
___OUTPUT___
**********
__________
hai silpa !
__________
**********
"""