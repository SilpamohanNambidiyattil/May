""" object oriented programming language"""
""" class
    object
    inheritence
    polymorphism
    encapsulation
    data abstraction"""
""" class : user defined templet
    object : An Object is an instance of a Class.
                instance is a copy of the class with actual values. 
    """
""" types of constructors
            parameterized
            non parameterized
            default parameterized"""
# class car():
#     s = "my car"
#     d = "iam silpa"
# a= car()
# print(a.s)
# print(a.d)
#
class CAR1():#self used to refer objects
    def __init__(self,car_name,car_model,car_color):#constructor used to initalize objects
        self.car_name = car_name
        self.car_model = car_model
        self.car_color = car_color
    def drive(self): # functions inside a class is called Method
        print("driving",self.car_name,self.car_model)
    def change_model(self):
        self.car_model=2024
        print("driving new model",self.car_name,self.car_model)

obj = CAR1("vento",2023,"grey")
print(obj.car_name)
print(obj.car_model)
print(obj.car_color)
print(obj.drive())
print(obj.change_model())

# #parameterized
# class Family:
#     # Constructor - parameterized
#     members = 5
#
#     def __init__(self, count):
#         print("This is parametrized constructor")
#         self.members = count
#
#     def show(self):
#         print("No. of members is", self.members)
#
#
# object = Family(10)
# object.show()
# #non parameterized
# class Fruits:
#     favourite = "Apple"
#
#     # non-parameterized constructor
#     def __init__(self):
#         self.favourite = "Orange"
#
#     # a method
#     def show(self):
#         print(self.favourite)
#
#
# # creating an object of the class
# obj = Fruits()
#
# # calling the instance method using the object obj
# obj.show()
#
# #Default
# class Assignments:
#     check= "not done"
#     # a method
#     def is_done(self):
#         print(self.check)
#
# # creating an object of the class
# obj = Assignments()
#
# # calling the instance method using the object obj
# obj.is_done()
#
#
