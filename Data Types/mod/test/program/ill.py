import math
v =[int(i) for i in  input("enter numbers :").split(',')]
print("Given list:",v)
num = [int(math.pow(i,2)) for i in v if int(i)%2!=0]
print(num)
#print(','.join(str(num)))