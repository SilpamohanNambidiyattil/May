class Teacher:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.__salary=salary
    def display(self):
        print(f"name:{self.name}, age:{self.age} ,salary:{self.__salary}")
tr=Teacher("silpa",25,30000)
tr.display()
#print(tr.__salary)  # error
print(tr.__dict__)
print(dir(tr))
