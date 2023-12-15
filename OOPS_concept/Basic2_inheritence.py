""" Multiple inheritance"""
""" child class have multiple parent class"""

class Vehicle:  # parent class
    def vehicle_info(self):
        print("inside vehicle class")

class Car:  # parent class
    def car_info(self):
        print("inside car class")

class Sportscar(Vehicle,Car):   # child class
    def sportscar_info(self):
        print("inside sportscar class")

obj=Sportscar()     # object of child class
obj.vehicle_info()      # child class object can access parent class method
obj.car_info()
obj.sportscar_info()

""" Multi level inheritance"""
