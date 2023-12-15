""" The circle class models a circle with a radius and color

attributes : radius , color

methods :

Circle
getRadius()
getCircumference()
getArea()"""
import math
class Circle:
    def __init__(self,radius,color):
        self.radius=radius
        self.color=color
    def getRadius(self):
        print("Radius:",self.radius)
    def getCircumference(self):
        circumference=2*math.pi*self.radius
        print("circumference:",circumference)
    def getArea(self):
        Area = math.pi*self.radius**2
        print("Area:",Area)

obj=Circle(100,'red')
obj.getRadius()
obj.getCircumference()
obj.getArea()

