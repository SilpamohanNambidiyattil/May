""" different forms of an object is polymorphism"""
#"""
class Vehicle:
    def __init__(self,name,color,price):
        self.name=name
        self.color=color
        self.price=price
    def show(self):
        print(f"Name:{self.name},Color:{self.color},Price:{self.price}")
    def max_speed(self):
        print("Maximum speed is 150")
    def change(self):
        print("changed")
class car(Vehicle):
    def show(self):
        print(f"Name:{self.name},Color:{self.color},Price:{self.price}")
    def max_speed(self):
        print("Maximum speed is 150 updated to 160")
    def change(self):
        print("changed again")
car =car('RR','White',1.5)
car.show()
car.max_speed()
car.change()
""""### OUTPUT ###
Name:RR,Color:White,Price:1.5
Maximum speed is 150 updated to 160
changed again"""
#"""
# import math
# class Shape:
#     def __init__(self,name):
#         self.name=name
#     def area(self):
#         pass
#     def fact(self):
#         return "iam a 2D shape"
#     def __str__(self):
#         return self.name
# class Square(Shape):
#     def __init__(self,length):
#         super().__init__("silpa'square")
#         self.length=length
#     def area(self):
#         return self.length**2
#     def fact(self):
#         return "All sides length are equal"
# class Circle(Shape):
#     def __init__(self,radius):
#         super().__init__("Silpa's Circle")
#         self.radius=radius
#     def area(self):
#         return math.pi*(self.radius**2)
#     def fact(self):
#         return "Diameter is twice the radius "
# sq=Square(4)
# ci=Circle(5)
# print(sq.name)
# print(sq.area())
# print(sq.fact())
# print("_____________________")
# print(ci.name)
# print(ci.area())
# print(ci.fact())
""""### OUTPUT ###
Silpa's Square
16
All sides length are equal
_____________________
Silpa's Circle
78.53981633974483
Diameter is twice the radius """
"""
class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Move!")
class Car(Vehicle):
    pass
class Ship(Vehicle):
    def move(self):
        print("Sail!")
class Plane(Vehicle):
    def move(self):
        print("Fly!")
obj_c=Car("bmw",2023)
obj_s=Ship("Kavarathy",2023)
obj_p=Plane("CR-7",2023)
for x in (obj_c,obj_s,obj_p):
    print(f"Brand:{x.brand},Model:{x.model}")
    x.move()
### OUTPUT ###
Brand:bmw,Model:2023
Move!
Brand:Kavarathy,Model:2023
Sail!
Brand:CR-7,Model:2023
Fly!
"""