""" wrapping up of data"""
""" access modifizes
    public 
    private
    protected"""
class Bank:
    def __init__(self,b_name,b_transaction,b_balance):
        self.name=b_name        # Public mode
        self._trans=b_transaction       # Protected mode (_)after self.
        self.__bal=b_balance        # Private Mode(__) after self.
    def test(self):
        print("Private mode balance in Parent class:",self.__bal)
class Customer(Bank):
    def bank_data(self):
        print("Bank name:",self.name)       # subclass can access the Public mode data
        print("Transcation:",self._trans)   # subclass can also access Protected mode data
        #print("Balance:",self.__bal)        # shows error because subclass cannod access private mode data
obj=Customer("SIB",12345678,100)
obj.bank_data()     # cannot access private mode attributes with a child class object
bank=Bank("Sib",458897,500)
bank.test()