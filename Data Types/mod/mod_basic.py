""" is a python program file which contains a python code including python functions ,
class , variables.....
extension .py
import statement
"""
import datetime


def sum(a,b):
    return a+b
print("Sum:",sum(4,2))

""" build in modules
ex: math 
import module
"""
import math
print("Square root:",math.sqrt(25))
print("Factorial:",math.factorial(5))

r=2
print("area:",math.pi*r*r)

""" os module 
performing operting system 
dict creating removing
 fecting content 
 used for file handeling
"""
import os
#os.mkdir(r"C:\Users\user\PycharmProjects\Operators\Data Types\mod\test")
#os.mkdir(r"C:\Users\user\PycharmProjects\Operators\Data Types\mod\test\sam")
#os.rmdir(r"C:\Users\user\PycharmProjects\Operators\Data Types\mod\test\sam")
print(os.getcwd())

""" os.chdir('D:/')
print(os.getcwd())"""

""" random module
 
import random """

import random
print("Random range:",random.randrange(10))
print("Random range :",random.randint(1,100))
a=[1,2,3,4,5,6,7,8,9,0]
random.shuffle(a)
print("Shuffle:",a)
str = 'silpa'
print("Choice :",random.choice(str))
print()


""" date time module"""
from _datetime import date
today = date.today()
print("Today Date :",today)
now = datetime.datetime.now()
print("Today Date and Time:",now)



""" Exter"""



