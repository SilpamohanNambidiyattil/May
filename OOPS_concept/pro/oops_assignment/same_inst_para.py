""" 3.Define a class, which have a class parameter and have a same
instance parameter.

Hints:
    Define a instance parameter, need add it in __init__ method
    You can inita object with construct parameter or set the value later
"""

class Person:
    attr1="python"# class parameter(parameter passed before constructor)
    def __init__(self,name):
        self.name="silpa"# instance parameter
        #self.name=name
    def get_info(self):
        print(self.name)
obj1 = Person("silpamohan")
obj2=Person("Silpa")
obj1.get_info()
print(obj2.attr1)
obj2.get_info()
