""" Define  a class which has atleast two methods:
getString:to get a string from console input
printString:to print the string in upper case
Also please include simple test function to test the class methods.
Hints:
use __init__ method to construct some parameters"""

class String_class:
    def __init__(self):
        self.string=''
    def getString(self):
        self.string=input("Enter the string:")
    def printString(self):
        print(f"upper case:{self.string.upper()}")
    def test(self):
        print("testing class methods")
str=String_class()
str.getString()
str.printString()
str.test()