""" Object Oriented Programming
    ____________________________
    
    * class --> plan,blue print,templet(design pattern)
    * object --> things constructed with this plan, blueprint .....
    * Syntax:
                class class_name:
                    attribute1
                    attribute2
                    attribute3...
                    method1():
                    method2():
                    ..........
                object_name=class_name()

self used to point object
    """

class Students:
    rollno:int
    name:str
    course:str
    
    def add_student(self,roll,name,course):
        self.rollno=roll
        self.name=name
        self.course=course
    def get_student(self):
        print(self.rollno,self.name,self.course)

obj1=Students()
obj1.add_student(123,"silpa","python")
obj1.get_student()

obj2=Students()
obj2.add_student(456,"reethu",'python')
obj2.get_student()