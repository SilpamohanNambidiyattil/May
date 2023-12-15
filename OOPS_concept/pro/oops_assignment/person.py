""" 9.Define a class Person and its two child classes: Male and Female.
All classes have a method
 "getGender" which can print "Male" for Male class and "Female" for Female class."""
class Person:
    def __init__(self,male,female):
        self.male=male
        self.female=female
class Male(Person):
    def getGender(self):
        print(f"Male class Gender:{self.male}")
class Female(Person):
    def getGender(self):
        print(f"Female class Gender:{self.female}")
obj1=Male("Male","Female")
obj1.getGender()
obj2=Female("Male","Female")
obj2.getGender()