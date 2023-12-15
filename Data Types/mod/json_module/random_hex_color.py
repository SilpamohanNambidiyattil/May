import random
import string
color = random.randrange(0,2**24)
hex_color = hex(color)
print("with hex function :",hex_color)
c="#%06x" % random.randint(0,0xffffff)
print("without hex function:",c)
s='python'
print(random.choice(s))
value = random.randrange(1,100)
print("Random value between 2 integers:",value)
mul = random.randint(0,70)
#print(mul)
print("Random multiple of 7 :",mul*7)