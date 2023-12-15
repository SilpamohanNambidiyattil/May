""" Create a class called Vehicle with the following attributes and methods:

Attributes:
make: a string representing the make of the vehicle
model: a string representing the model of the vehicle
year: an integer representing the year the vehicle was made
color: a string representing the color of the vehicle
mileage: a float representing the current mileage of the vehicle

Methods:
_init_(self, make, model, year, color, mileage): initializes the attributes
 with the given values.
drive(self, distance): takes a float representing the distance driven and
updates the mileage attribute accordingly.
get_info(self): returns a string with the vehicle's make, model, year,
 color, and mileage attributes in a formatted way.
 Create a subclass called Car that inherits from the Vehicle class with
the following additional attributes and methods:
Attributes:
num_doors: an integer representing the number of doors the car has
engine_type: a string representing the type of engine the car has
Methods:
_init_(self, make, model, year, color, mileage, num_doors, engine_type):
 initializes the attributes with the given values.
get_info(self): overrides the get_info method of the Vehicle class to
 include the num_doors and engine_type attributes.
Create an instance of the Vehicle class and call the drive method with a
 distance of 100. Then call the get_info method to print out the vehicle's information.

Create an instance of the Car class and call the drive method with a distance of 50.
Then call the get_info method to print out the car's information.
Define a class, which have a class parameter and have a same instance parameter.

Hints:
    Define a instance parameter, need add it in init method
    You can init a object with construct parameter or set the value later"""

class Vehicle:
    def __init__(self,make,model):
        self.make=make
        self.model = model
        # self.year = year
        # self.color = color
        # self.mileage = mileage
    # def drive(self,distance):
    #     print("Initial Mileage",self.mileage)
    #     self.mileage=self.mileage+distance
    #     print("updated mileage:",self.mileage)
    # def get_info(self):
    #     print(f"Make:{self.make},Model:{self.model},Year:{self.year},Color:{self.color},Mileage:{self.mileage}")
    def display(self):
        print(self.make,self.model)

class Car(Vehicle):
    def __init__(self,make,model,num_doors,engine_type):
        super().__init__(make,model)
        # self.make=make
        # self.model=model
        self.num_doors= num_doors
        self.engine_type=engine_type
    # def get_info(self):
    #     #vehicle_info=super().get_info()
    #     print(f"Make:{self.make},Model:{self.model},Year:{self.year},Color:{self.color},Mileage:{self.mileage},Doors:{self.num_doors},Engine_type:{self.engine_type}")
    def pr(self):
        print(self.make,self.model,self.num_doors,self.engine_type)


obj_v = Vehicle('BMW_3_s',2020)
# obj_v.drive(100)
# obj_v.get_info()
print("___________________________________________")
# obj_c = Car("BMW_5_s",'2023',2023,"black",20.0,4,'petrol')
obj_car=Car("bmw",2023,4,"petrol")
obj_car.pr()