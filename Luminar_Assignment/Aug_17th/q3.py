""" 3.Write a Python class Square, and define two methods that return the square area and perimeter."""

class Square:
    side:float
    def set_side(self,side):
        self.side=side
    def area(self):
        area_sq = self.side**2
        print("Area of Square:",area_sq)
    def peri(self):
        peri_sq= 4*self.side
        print("Perimeter of Square:",peri_sq)

obj=Square()
obj.set_side(2)
obj.area()
obj.peri()

"""
OUTPUT
Area of Square: 4
Perimeter of Square: 8
"""