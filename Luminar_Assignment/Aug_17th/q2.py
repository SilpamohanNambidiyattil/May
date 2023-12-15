""" 2. Write a program to create a child class Teacher that will inherit the properties of Parent 
 Staf"""

class Staff:
   department:str
   def __init__(self,department) -> None:
       self.department=department
class Teacher(Staff):
    name=str
    subject=str
    def __init__(self,department,name,subject) -> None:
        super().__init__(department)
        self.name=name
        self.subject=subject
    def display(self):
        print(f"Name:{self.name},Department:{self.department},Subject:{self.subject}")
obj=Teacher("Computer Science","Silpa","Computer Networks")
obj.display()

"""
OUTPUT
Name:Silpa,Department:Computer Science,Subject:Computer Networks
"""
