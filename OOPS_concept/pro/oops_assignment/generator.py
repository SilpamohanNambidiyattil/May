""" 2.Define a class with a generator which can iterate the numbers,
which are divisible by 7, between a given range 0 and n.
(Just try )

Hints:
Consider use yield

"""
class Generator:
    def __init__(self,n):
        self.n=n
    def gen(self):
        for i in range(0,self.n):
            if i%7==0:
                #yield i
                print(i)
gen=Generator(20)
gen.gen()
#print(gen.gen())