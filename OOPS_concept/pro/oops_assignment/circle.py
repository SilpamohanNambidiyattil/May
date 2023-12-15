"""6.Define a class named Circle which can be constructed by a radius.
The Circle class has a method which can compute the area.

Hints:

Use def methodName(self) to define a method.
 """
import math
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def Area(self):
        Area = math.pi*self.radius**2
        print("Area:",Area)

obj=Circle(5)
obj.Area()
