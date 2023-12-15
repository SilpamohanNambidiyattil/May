"""8.Define a class named Shape and its subclass Square.
 The Square class has an init function which takes a length as argument.
 Both classes have a area function which can print the area of the shape where
  Shape's area is 0 by default.

Hints:

To override a method in super class, we can define a method with the same name in
 the super class.

"""
class Shape:
    def __init__(self,area):
        self.area=0
    def Area(self):
        print("Area of Shape",self.area)
class Square(Shape):
    def __init__(self,length):
        self.length=length
    def Area(self):
        area=self.length**2
        print(f"Area of Square:",area)
obj= Square(5)
obj.Area()
obj1=Shape(5)
obj1.Area()

