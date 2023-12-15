import json
x = {'name':"reethu", "age": 28 , "course": "python" , "guide": "priya"}
print(x)
y = json.dumps(x)
print(y)
print(type(y))

a= y.split()
print(a)
z1,z2=a[3],a[5]
print (z1,z2)
#print(y["age"], y["course"])

