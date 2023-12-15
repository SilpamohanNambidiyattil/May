# class Myclass:
#     class_variable = 'silpa'
#     @classmethod
#     def class_method(cls):
#         print(cls.class_variable)
# Myclass.class_method()
# obj = Myclass()
# obj.class_method()


class Rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b
    def peri(self):
        return 2*(self.l+self.b)
    @classmethod
    def crete_square(cls,side):
        return cls(side*side)
rectangle=Rectangle(2,4)
print(rectangle.area())
print(rectangle.peri())


square=Rectangle.crete_square(4)
print(square.area())
print(square.peri())


# class Bank:
#     interest_rate=0.8
#     def __init__(self,account_number,balance):
#         self.account_number=account_number
#         self.balance=balance
#     def deposite(self,amount):
#         self.balance=self.balance+ amount
#         print(f"Balance after deposite:{self.balance}")
#     def withdraw(self,amount):
#         if self.balance>=amount:
#             self.balance=self.balance-amount
#             print(f"Balance after withdraw:{self.balance}")
#         else:
#             print("insufficient fund")
#     def calculate_interest(self):
#         cal=self.balance*self.interest_rate
#         print(f"interest calculated:",cal)
#     @classmethod
#     def set_interest_rate(cls,rate):
#         cls.interest_rate=rate
# bank=Bank("sib112345",500)
# bank.deposite(100)
# bank.withdraw(400)
# bank.calculate_interest()
# #Bank.interest_rate()
# #bank.interest_rate()
# obj=Bank.set_interest_rate(0.07)
# print(obj)
# interest=bank.calculate_interest()
# print(interest)
