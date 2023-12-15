""" 4.define an account class with attributes ac no,ac name,balance"""

class Account:
    ac_no:int
    ac_name:str
    balance:float
    def set_account(self,ac_no,ac_name,balance):
        self.ac_no=ac_no
        self.ac_name=ac_name
        self.balance=balance
    def get_ac(self):
        print(f"Name:{self.ac_name},Account_No:{self.ac_no},Balance:{self.balance}")
    
bank=Account()
bank.set_account(1234567890,"Silpa",5000)
bank.get_ac()
print(bank.ac_name)
print(bank.ac_no,bank.balance)

"""
OUTPUT
Name:Silpa,Account_No:1234567890,Balance:5000
Silpa
1234567890 5000
"""