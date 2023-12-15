class Employee:
    id:int
    name:str
    desig:str
    salary:int

    def set_employee(self,id,name,desig,salary):
        self.id=id
        self.name=name
        self.desig=desig
        self.salary=salary

    def get_employee(self):
        print(self.id, self.name, self.desig, self.salary)

obj1=Employee()
obj1.set_employee(1,"silpa","developer",50000)
obj1.get_employee()
# dir function used to get all details of an object
print(dir(obj1))
print(obj1.__class__)