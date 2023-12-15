""" 5.Create classes for a school management system. Have classes like Student, Teacher, and Course. 
Implement methods to enroll students, assign teachers, and display course details."""

# class Student:
#     name:str
#     def _str_(self,name):
#         self.name=kwargs.get("name")
#     def enroll_students(self,**kwargs):
#         return self.name

# class Teacher:
#     assign: str

#     def _str_(self, assign):
#         self.assign = kwargs.get("assign")
#     def assign_teachers(self,**kwargs):
#         return self.assign
# class Course:
#     display: str

#     def _init_(self, display):
#         self.display = kwargs.get("display")
#     def display_course_details(self,**kwargs):
#         return self.display
# obj=Student()

# print(obj.enroll_students(name="reethu"))

# obj1=Teacher()
# print(obj1.assign_teachers(assign="science"))
# obj3=Course()
# print(obj3.display_course_details(display="bscmaths"))

class Student:
    student_id:int
    name:str
    age:int
    def __init__(self,student_id,name,age):
        self.student_id=student_id
        self.name=name
        self.age=age
    def enroll(self):
        print(f"Student_id {self.student_id}  {self.name} student of age {self.age} should report in office")

class Teacher:
    def __init__(self,teacher_id,name,subject):
        self.teacher_id=teacher_id
        self.name=name
        self.subject=subject
    def assign_teachers(self):
        print(f"Teacher_id {self.teacher_id} {self.name} teacher must teach the subject {self.subject}")

class Course:
    def __init__(self,course_code,course_name):
        self.course_code=course_code
        self.course_name=course_name

    def display_coursedetails(self):
        print("course code:",self.course_code)
        print("course name:",self.course_name)



student=Student(1,"Silpamohan N",25)
student.enroll()

teacher=Teacher(1,"","Computer Networks")
teacher.assign_teachers()

course=Course(234,"Computer Science")
course.display_coursedetails()

"""
OUTPUT
Student_id 1  Silpamohan N student of age 25 should report in office
Teacher_id 1  teacher must teach the subject Computer Networks
course code: 234
course name: Computer Science
"""