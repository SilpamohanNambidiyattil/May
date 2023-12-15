""" over ridding"""

class Animal:
    def __init__(self,name):
        self.name= name
    def breath(self):
        print("i breath oxygen")
    def food(self):
        print("i eat food")
class Dog(Animal):
    def food(self):
        print("i love non-veg food")
obj=Dog("Rodger")
obj.food() #output: i love non-veg food
obj.breath()#output: i breath oxygen