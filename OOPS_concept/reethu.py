class Dog:
    attr1 = "mammal"
    def __init__(self,name):
        self.name=name
obj = Dog("rodger")
print("Rodger is a {}".format(obj.__class__.attr1))
print("Tommy is a {}".format(obj.__class__.attr1))

obj1=Dog("rodger")
print(obj1.attr1)
print("My name is {}".format(obj1.name))
