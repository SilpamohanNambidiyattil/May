"""1. Write a Program to create a class by name Students, and initialize attributes like name,
 age, and grade while creating an object.
 """
class Students:
    name:str
    age:int
    grade:str
    def set_student(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def get_info(self):
        print(f"Name:{self.name},Age:{self.age},Grade:{self.grade}")
obj=Students()
obj.set_student("Silpa",25,"A")
obj.get_info()

"""
OUTPUT
Name:Silpa,Age:25,Grade:A
"""