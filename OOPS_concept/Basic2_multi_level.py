""" Multi level inheritance"""

class Vehicle:  # parent class
    def vehicle_info(self):
        print("inside vehicle class")

class Car(Vehicle):  # intermediate class it contains properties of vehicle class
    def car_info(self):
        print("inside car class")

class Sportscar(Car):   # child class it contains both the properties of  car and vehicle class
    def sportscar_info(self):
        print("inside sportscar class")

obj = Sportscar()   #ojbect of child class
obj.vehicle_info()
obj.car_info()
obj.sportscar_info()

