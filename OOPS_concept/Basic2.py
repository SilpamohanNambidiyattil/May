""" inheritence"""
""" her"""
""" parent class called supper class or base class
child class is called derived class or subclass
Advantage : code reuseability"""

""" Single inheritence"""

""" over ridding redefining a pc method in derived class
    over loading 2 or more methods with same name but different parameters"""
class Animals: #parent class
    def __init__(self,name,category): #constructor
        self.name=name
        self.category=category
    def test(self):
        print("Parent class")
        pass#empty statement so not shows any error

class Dog(Animals):#derived class [pass Animal as parameter]
    def speak(self):
        print('Dog name is',self.name)

class Cat(Animals):# self.name inherited for dog and cat from Animals
    def speak(self):
        print('Cat name is',self.name,self.category)
obj_dog=Dog("rockey",'black')
obj_cat=Cat("kitty","white")
obj_dog.speak()
obj_dog.test()# by using child class object we can access parent clss methods
obj_cat.speak()

