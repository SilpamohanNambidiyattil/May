class Bank:
    acno:int
    balance:float
    ac_type:str
    p_name:str
    def create_account(self,acno,balance,ac_type,p_name):
        self.acno=acno
        self.balance=balance
        self.ac_type=ac_type
        self.p_name=p_name
        print(f"Name:{self.p_name},Account_type:{self.ac_type},Account_number:{self.acno},Balance:{self.balance}")
    def deposit(self,amount):
        bal=self.balance+amount
        print("balance after deposit:",bal)
    def withdraw(self,amount):
        bala=self.balance-amount
        print("balance after withdraw",bala)

bank1=Bank()
bank1.create_account(12345,5000,"savings","Silpa")
bank1.deposit(200)
bank1.withdraw(1000)