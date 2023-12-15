"""7.Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area.

Hints:

Use def methodName(self) to define a method.

"""
class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def Area(self):
        Area = self.length*self.breadth
        print("Area:",Area)

obj=Rectangle(5,2)
obj.Area()