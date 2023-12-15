# """ hide unneccessary informations from user and shows informations according
# to users requirment"""
# from abc import ABC, abstractmethod# abc already build
# class Shape(ABC):   # Abstract class
#     @abstractmethod # decorator
#     def area(self):
#         area=90
#         print("area inside shape class:",area)
#
#     def display(self):
#         print("inside shape class!!!!!!!")
# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return 3.14*self.radius**2
# class Rectangle(Shape):
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#
#     def area(self):
#         return self.length*self.width
# circle=Circle(5)
# rect=Rectangle(4,6)
# print("area of circle:",circle.area())
# print("area of rectangle:",rect.area())
# circle.area(7)
# rect.display(9)
#
#
#
#
#
#
#
from abc import ABC, abstractmethod


class Absclass(ABC):
    def print(self, x):
        print("Passed value: ", x)

    @abstractmethod
    def task(self):
        print("We are inside Absclass task")


class test_class(Absclass):
    def task(self):
        print("We are inside test_class task")


class example_class(Absclass):
    def task(self):
        print("We are inside example_class task")


# object of test_class created
test_obj = test_class()
test_obj.task()
test_obj.print(100)

# object of example_class created
example_obj = example_class()
example_obj.task()
example_obj.print(200)

print("test_obj is instance of Absclass? ", isinstance(test_obj, Absclass))
print("example_obj is instance of Absclass? ", isinstance(example_obj, Absclass))


""" Absclass is the abstract class that inherits from the ABC class from 
the abc module. It contains an abstract method task() and a print() method which 
are visible by the user. Two other classes inheriting from this abstract class are 
test_class and example_class. Both of them have their own task() method 
(extension of the abstract method).

After the user creates objects from both the test_class and
 example_class classes and invoke the task() method for both of them, 
 the hidden definitions for task() methods inside both the classes come into play.
  These definitions are hidden from the user. The abstract method task() from
   the abstract class Absclass is actually never invoked."""
