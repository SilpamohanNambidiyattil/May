def my_func(**kid):
    print("His last name is " + kid['lname'])
my_func(fname='Silpamohan',lname='N')

def my(fname,lname):
    print(fname + " " + lname)
my("Silpamohan","N")

def my_(fname):
    print(fname + ' ' 'N')
my_('Silpamohan')
my_('Akshaymohan')
x = lambda a : a + 10
print(x(5))