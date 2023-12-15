""" Hierarchical inheritance Similar to single but different child class is
 there"""
""" Hybird inheritance is the combination of different inheritance"""

class Vehicle:  # parent class
    def vehicle_info(self):
        print("inside vehicle class")

class Car(Vehicle):  # intermediate class it contains properties of vehicle class
    def car_info(self):
        print("inside car class")

class Truck(Vehicle):  # intermediate class it contains properties of vehicle class
    def truck_info(self,name):
        print("truck name:",name)

class Sportscar(Car,Truck):   # child class it contains both the properties of  car and truck class
    def sportscar_info(self):
        print("inside sportscar class")

obj = Sportscar()   #ojbect of child class
obj.vehicle_info()
obj.car_info()
obj.sportscar_info()
obj.truck_info('TATA')