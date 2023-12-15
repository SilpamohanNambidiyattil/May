class Staff:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    def show_details(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Role:", self.role)
        print("Department:", self.dept)
        print("Salary:",self.salary)
#inherit from the Staff class
class Teacher(Staff):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # initialize the Parent  class
        super().__init__("Teacher", "Science", 25000)
teacher = Teacher("Raj", 28)
#access the Staff Method
teacher.show_details()
print(teacher.__dict__)
# print(teacher.name,sep=" ")

# class Animal:
#     def __init__(self,identity,age):
#         self.identity=identity
#         self.age=age
#     def feature(self):
#         if self.age==10:
#             return True
#         else:
#             return False
# Ac=Animal("lion",9)
# print(Ac.__dict__)
# print(Ac.feature())


# class Rect:
#     def __init__(self,l,b):
#         self.l=l
#         self.b=b
#     def __str__(self):
#         return f"Rectangle with length:{self.l} and width:{self.b}"
# rect=Rect(6,8)
# print(rect.__str__())
# print(rect.__dict__)    # using __dict__